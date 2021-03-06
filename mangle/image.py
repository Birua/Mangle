﻿# Copyright (C) 2010  Alex Yatskov
# Copyright (C) 2011  Stanislav (proDOOMman) Kosolapov <prodoomman@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from PIL import Image, ImageDraw, ImageStat, ImageFile
import zipfile, rarfile

class ImageFlags:
    Orient = 1 << 0
    Resize = 1 << 1
    Frame = 1 << 2
    Quantize = 1 << 3
    Split = 1 << 4
    Reverse = 1 << 5
    Cbz = 1 << 6
    Crop = 1 << 7
    CutNumbers = 1 << 8
    ProgressBar = 1 << 9


class KindleData:
    Palette4 = [
        0x00, 0x00, 0x00,
        0x55, 0x55, 0x55,
        0xaa, 0xaa, 0xaa,
        0xff, 0xff, 0xff
    ]

    Palette15a = [
        0x00, 0x00, 0x00,
        0x11, 0x11, 0x11,
        0x22, 0x22, 0x22,
        0x33, 0x33, 0x33,
        0x44, 0x44, 0x44,
        0x55, 0x55, 0x55,
        0x66, 0x66, 0x66,
        0x77, 0x77, 0x77,
        0x88, 0x88, 0x88,
        0x99, 0x99, 0x99,
        0xaa, 0xaa, 0xaa,
        0xbb, 0xbb, 0xbb,
        0xcc, 0xcc, 0xcc,
        0xdd, 0xdd, 0xdd,
        0xff, 0xff, 0xff,
    ]

    Palette15b = [
        0x00, 0x00, 0x00,
        0x11, 0x11, 0x11,
        0x22, 0x22, 0x22,
        0x33, 0x33, 0x33,
        0x44, 0x44, 0x44,
        0x55, 0x55, 0x55,
        0x77, 0x77, 0x77,
        0x88, 0x88, 0x88,
        0x99, 0x99, 0x99,
        0xaa, 0xaa, 0xaa,
        0xbb, 0xbb, 0xbb,
        0xcc, 0xcc, 0xcc,
        0xdd, 0xdd, 0xdd,
        0xee, 0xee, 0xee,
        0xff, 0xff, 0xff,
    ]

    Profiles = {
        'Kindle 1': ((600, 800), Palette4),
        'Kindle 2': ((600, 800), Palette15a),
        'Kindle 3': ((600, 800), Palette15a),
        'Kindle 4': ((600, 800), Palette15b),
        'Kindle DX': ((824, 1200), Palette15a),
        'Kindle DXG': ((824, 1200), Palette15a)
    }


def quantizeImage(image, palette):
    colors = len(palette) / 3
    if colors < 256:
        palette = palette + palette[:3] * (256 - colors)

    palImg = Image.new('P', (1, 1))
    palImg.putpalette(palette)

    return image.quantize(palette=palImg)


def resizeImage(image, size):
    widthDev, heightDev = size
    widthImg, heightImg = image.size

#    if widthImg <= widthDev and heightImg <= heightDev:
#        return image

    ratioImg = float(widthImg) / float(heightImg)
    ratioWidth = float(widthImg) / float(widthDev)
    ratioHeight = float(heightImg) / float(heightDev)

    if ratioWidth > ratioHeight:
        widthImg = widthDev
        heightImg = int(widthDev / ratioImg)
    elif ratioWidth < ratioHeight:
        heightImg = heightDev
        widthImg = int(heightDev * ratioImg)
    else:
        widthImg, heightImg = size

    return image.resize((widthImg, heightImg), Image.ANTIALIAS)


def formatImage(image):
    if image.mode == 'RGB':
        return image
    return image.convert('RGB')


def orientImage(image, size):
    widthDev, heightDev = size
    widthImg, heightImg = image.size

    if (widthImg > heightImg) != (widthDev > heightDev):
        return image.rotate(90, Image.BICUBIC, True)

    return image


def frameImage(image, foreground, background, size):
    widthDev, heightDev = size
    widthImg, heightImg = image.size

    pastePt = (
        max(0, (widthDev - widthImg) / 2),
        max(0, (heightDev - heightImg) / 2)
    )

    corner1 = (
        pastePt[0] - 1,
        pastePt[1] - 1
    )

    corner2 = (
        pastePt[0] + widthImg + 1,
        pastePt[1] + heightImg + 1
    )

    imageBg = Image.new(image.mode, size, background)
    imageBg.paste(image, pastePt)

    draw = ImageDraw.Draw(imageBg)
    draw.rectangle([corner1, corner2], outline=foreground)

    return imageBg


def cutPageNumber(image):

    widthImg, heightImg = image.size

    delta = 2 # Зададим шаг
    diff = delta
    fixedThreshold = 5

    #Защита от чистого листа
    if ImageStat.Stat(image).var[0] < 2*fixedThreshold:
        return image

    while ImageStat.Stat(image.crop((0,heightImg-diff,widthImg,heightImg))).var[0] < fixedThreshold \
    and diff < heightImg:
        diff += delta
    diff -= delta

    # Дальше сканируем вероятный номер на странице
    pageNumberCut1=diff #Расстояние снизу до вероятного номера страницы
    if diff<delta:
       diff=delta
    oldStat=ImageStat.Stat(image.crop((0,heightImg-diff,widthImg,heightImg))).var[0]
    diff += delta
    while ImageStat.Stat(image.crop((0,heightImg-diff,widthImg,heightImg))).var[0] - oldStat > 0 \
    and diff < heightImg/4:
        oldStat=ImageStat.Stat(image.crop((0,heightImg-diff,widthImg,heightImg))).var[0]
##        print '1',diff,oldStat
        diff += delta
    diff -= delta
    pageNumberCut2=diff #Расстояние снизу включая номер страницы

    #Сканируем вероятную белую полосу над номером
    diff += delta
    oldStat=ImageStat.Stat(image.crop((0,heightImg-diff,widthImg,heightImg-pageNumberCut2))).var[0]
    while ImageStat.Stat(image.crop((0,heightImg-diff,widthImg,heightImg-pageNumberCut2))).var[0] < fixedThreshold+oldStat \
    and diff < heightImg/4:
##        print '2',diff
        diff += delta
    diff -= delta
    pageNumberCut3=diff #Расстояние снизу до картинки включая номер страницы и белую полосу

    #Определим ширину номера страницы
    #================================
    delta = 5 # Изменим шаг

    diff = delta
    while ImageStat.Stat(image.crop((0,heightImg-pageNumberCut2,diff,heightImg))).var[0] < fixedThreshold \
    and diff < widthImg:
        diff += delta
    diff -= delta
    pageNumberX1 = diff #X координата начала номера страницы

    diff = delta
    while ImageStat.Stat(image.crop((widthImg-diff,heightImg-pageNumberCut2,widthImg,heightImg))).var[0] < fixedThreshold \
    and diff < widthImg:
        diff += delta
    diff -= delta
    pageNumberX2=widthImg-diff #X координата конца номера страницы

##    print pageNumberCut1,pageNumberCut2,pageNumberCut3

    #Логика: номер и полоса сверху должны быть больше 2*дельта, иначе не стоит вырезать;
    #        ширина номера должна быть не более чем в 9.0 раз больше высоты, иначе - это коммент;
    #        ну и не резать выше четверти картинки, чтоб не наглеть;
    #        также не вырезать больше 1/10 от .Stat().var[0] картинки
    #Возможно параметр ширина/высота (9.0) стоит дать менять?
    #пока подобрал его по своим примерам, для самого широкого варианта
    if pageNumberCut3-pageNumberCut1 > 2*delta and \
       float(pageNumberX2-pageNumberX1)/float(pageNumberCut2-pageNumberCut1) <= 9.0 and \
       ImageStat.Stat(image.crop((0,heightImg-pageNumberCut3,widthImg,heightImg))).var[0] / ImageStat.Stat(image).var[0] < 0.1 and \
       pageNumberCut3 < heightImg/4-delta:
      diff=pageNumberCut3
##      print 'Cutting page number!',pageNumberCut3-pageNumberCut1,'pixels saved!'
    else:
      diff=pageNumberCut1

##    print pageNumberCut3-pageNumberCut1 > 2*delta, \
##          ImageStat.Stat(image.crop((0,heightImg-pageNumberCut3,widthImg,heightImg))).var[0] / ImageStat.Stat(image).var[0], \
##          float(pageNumberX2-pageNumberX1)/float(pageNumberCut2-pageNumberCut1), \
##          pageNumberCut3 < heightImg/4-delta
##
##    #Draw to debug
##
##    draw = ImageDraw.Draw(image)
##    #Black rectangle
##    draw.rectangle([(0,heightImg-pageNumberCut1), (widthImg,heightImg)], outline=0)
##    draw.rectangle([(pageNumberX1,heightImg-pageNumberCut2), (pageNumberX2,heightImg)], outline=0)
##    draw.rectangle([(20,heightImg-pageNumberCut3), (widthImg-20,heightImg)], outline=0)

#    print "Down crop: %s"%diff
    image = image.crop((0,0,widthImg,heightImg-diff))

    return image

def cropWhiteSpace(image, threshold):
#    print "Old size: %sx%s"%(image.size[0],image.size[1])
    widthImg, heightImg = image.size
    delta = 10
    diff = delta
    # top
    while ImageStat.Stat(image.crop((0,0,widthImg,diff))).var[0] < threshold \
    and diff < heightImg:
        diff += delta
    diff -= delta
#    print "Top crop: %s"%diff
    image = image.crop((0,diff,widthImg,heightImg))
    widthImg, heightImg = image.size
    diff = delta
    # left
    while ImageStat.Stat(image.crop((0,0,diff,heightImg))).var[0] < threshold \
    and diff < widthImg:
        diff += delta
    diff -= delta
#    print "Left crop: %s"%diff
    image = image.crop((diff,0,widthImg,heightImg))
    widthImg, heightImg = image.size
    diff = delta
    # down
    while ImageStat.Stat(image.crop((0,heightImg-diff,widthImg,heightImg))).var[0] < threshold \
    and diff < heightImg:
        diff += delta
    diff -= delta
#    print "Down crop: %s"%diff
    image = image.crop((0,0,widthImg,heightImg-diff))
    widthImg, heightImg = image.size
    diff = delta
    # right
    while ImageStat.Stat(image.crop((widthImg-diff,0,widthImg,heightImg))).var[0] < threshold \
    and diff < widthImg:
        diff += delta
    diff -= delta
#    print "Right crop: %s"%diff
    image = image.crop((0,0 ,widthImg-diff,heightImg))
#    print "New size: %sx%s"%(image.size[0],image.size[1])
    return image

def add_progressbar(image, file_number, files_totalnumber, size, howoften):

  if file_number//howoften!=float(file_number)/howoften:
    return image

  widthImg, heightImg = image.size

  #========================================================================
  #Сделаем картинку полной по ширине, для одинаковых размеров прогресс бара

  white = (255,255,255) #Белый цвет
  black = (0,0,0) #Черный цвет

  widthDev, heightDev = size
  widthImg, heightImg = image.size

  pastePt = (
        max(0, (widthDev - widthImg) / 2),
        max(0, (heightDev - heightImg) / 2)
    )

  imageBg = Image.new('RGB',size,white)

  imageBg.paste(image, pastePt)
  image=imageBg
  widthImg, heightImg = image.size

  #========================================================================

  draw = ImageDraw.Draw(image)
  #Black rectangle
  draw.rectangle([(0,heightImg-3), (widthImg,heightImg)], outline=black, fill=black)
  #White rectangle
  draw.rectangle([(widthImg*file_number/files_totalnumber,heightImg-3), (widthImg-1,heightImg)], outline=black, fill=white)

  #Making notches
  for i in range(1,10):
    if i <= (10*file_number/files_totalnumber):
        notch_colour=white #White
    else:
        notch_colour=black  #Black
    draw.line([(widthImg*float(i)/10,heightImg-3), (widthImg*float(i)/10,heightImg)],fill=notch_colour)
    #The 50%
    if i==5:
        draw.rectangle([(widthImg/2-1,heightImg-5), (widthImg/2+1,heightImg)],outline=black,fill=notch_colour)

  return image

def convertImage(source, target, index, device, flags, crop_threshold, file_number, files_totalnumber, progressBar):
    try:
        size, palette = KindleData.Profiles[device]
    except KeyError:
        raise RuntimeError('Unexpected output device %s' % device)

    try:
        if source.startswith("ZIP://") and " NAME://" in source:
            try:
                archivename, filename = source.split(" NAME://")
                archivename = archivename[6:]
                image_io = ImageFile.Parser()
                archive = zipfile.ZipFile(archivename)
		try:
                    image_io.feed(archive.read(filename))
		except KeyError:
		    image_io.feed(archive.read(filename.encode("cp866")))
                image = image_io.close()
            except RuntimeError:
                raise RuntimeError('Cannot read image file %s' % source)
	elif source.startswith("RAR://") and " NAME://" in source:
            try:
                archivename, filename = source.split(" NAME://")
                archivename = archivename[6:]
                image_io = ImageFile.Parser()
                archive = rarfile.RarFile(archivename)
                image_io.feed(archive.read(filename))
                image = image_io.close()
            except RuntimeError:
                raise RuntimeError('Cannot read image file %s' % source)
        else:
            image = Image.open(source)
    except IOError:
        raise RuntimeError('Cannot read image file %s' % source)
    image = formatImage(image)
    delta = 0
    count = 1
    split = False
    widthDev, heightDev = size
    widthImg, heightImg = image.size
    if flags & ImageFlags.Split and (widthImg > heightImg) != (widthDev > heightDev):
        count += 1
        split = True
    boxlist = [(0,0,widthImg/2,heightImg),(widthImg/2,0,widthImg,heightImg)]
    targets = []
    while count>0:
        if split:
            if flags & ImageFlags.Reverse:
                tmp_image = image.crop(boxlist[(count+1)%2])
            else:
                tmp_image = image.crop(boxlist[count%2])
        else:
            tmp_image = image
        if flags & ImageFlags.CutNumbers:
            tmp_image = cutPageNumber(tmp_image)
        if flags & ImageFlags.Crop:
            tmp_image = cropWhiteSpace(tmp_image, crop_threshold)
        if flags & ImageFlags.Orient:
            tmp_image = orientImage(tmp_image, size)
        if flags & ImageFlags.Resize:
            tmp_image = resizeImage(tmp_image, size)
        if flags & ImageFlags.Frame:
            tmp_image = frameImage(tmp_image, tuple(palette[:3]), tuple(palette[-3:]), size)
        if flags & ImageFlags.ProgressBar:
            tmp_image = add_progressbar(tmp_image, file_number,files_totalnumber, size, progressBar)
        if flags & ImageFlags.Quantize:
            tmp_image = quantizeImage(tmp_image, palette)
        try:
            tmp_image.save(target%(index+delta))
        except IOError:
            raise RuntimeError('Cannot write image file %s' % target%(index+delta))
        targets.append(target%(index+delta))
        delta += 1
        count -= 1

    return targets
