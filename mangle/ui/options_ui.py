# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options.ui'
#
# Created: Thu Feb 16 22:35:09 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogOptions(object):
    def setupUi(self, DialogOptions):
        DialogOptions.setObjectName(_fromUtf8("DialogOptions"))
        DialogOptions.resize(701, 560)
        self.gridLayout = QtGui.QGridLayout(DialogOptions)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(DialogOptions)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEditTitle = QtGui.QLineEdit(self.groupBox)
        self.lineEditTitle.setObjectName(_fromUtf8("lineEditTitle"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditTitle)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(DialogOptions)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(DialogOptions)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.prevOrig = ImageContainer(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prevOrig.sizePolicy().hasHeightForWidth())
        self.prevOrig.setSizePolicy(sizePolicy)
        self.prevOrig.setBaseSize(QtCore.QSize(0, 0))
        self.prevOrig.setFrameShape(QtGui.QFrame.StyledPanel)
        self.prevOrig.setText(_fromUtf8(""))
        self.prevOrig.setPixmap(QtGui.QPixmap(_fromUtf8(":/img/preview/page.png")))
        self.prevOrig.setAlignment(QtCore.Qt.AlignCenter)
        self.prevOrig.setObjectName(_fromUtf8("prevOrig"))
        self.gridLayout_2.addWidget(self.prevOrig, 0, 0, 1, 2)
        self.prevPage1 = ImageContainer(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prevPage1.sizePolicy().hasHeightForWidth())
        self.prevPage1.setSizePolicy(sizePolicy)
        self.prevPage1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.prevPage1.setText(_fromUtf8(""))
        self.prevPage1.setAlignment(QtCore.Qt.AlignCenter)
        self.prevPage1.setObjectName(_fromUtf8("prevPage1"))
        self.gridLayout_2.addWidget(self.prevPage1, 1, 0, 1, 1)
        self.prevPage2 = ImageContainer(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prevPage2.sizePolicy().hasHeightForWidth())
        self.prevPage2.setSizePolicy(sizePolicy)
        self.prevPage2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.prevPage2.setText(_fromUtf8(""))
        self.prevPage2.setAlignment(QtCore.Qt.AlignCenter)
        self.prevPage2.setObjectName(_fromUtf8("prevPage2"))
        self.gridLayout_2.addWidget(self.prevPage2, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 1, 1, 2, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.prevPreviewButton = QtGui.QToolButton(DialogOptions)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/go-previous.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prevPreviewButton.setIcon(icon)
        self.prevPreviewButton.setObjectName(_fromUtf8("prevPreviewButton"))
        self.horizontalLayout.addWidget(self.prevPreviewButton)
        self.previewSpinBox = QtGui.QSpinBox(DialogOptions)
        self.previewSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.previewSpinBox.setMinimum(-1)
        self.previewSpinBox.setProperty("value", -1)
        self.previewSpinBox.setObjectName(_fromUtf8("previewSpinBox"))
        self.horizontalLayout.addWidget(self.previewSpinBox)
        self.nextPreviewButton = QtGui.QToolButton(DialogOptions)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/go-next.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextPreviewButton.setIcon(icon1)
        self.nextPreviewButton.setObjectName(_fromUtf8("nextPreviewButton"))
        self.horizontalLayout.addWidget(self.nextPreviewButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(DialogOptions)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.comboBoxDevice = QtGui.QComboBox(self.groupBox_2)
        self.comboBoxDevice.setObjectName(_fromUtf8("comboBoxDevice"))
        self.comboBoxDevice.addItem(_fromUtf8(""))
        self.comboBoxDevice.addItem(_fromUtf8(""))
        self.comboBoxDevice.addItem(_fromUtf8(""))
        self.comboBoxDevice.addItem(_fromUtf8(""))
        self.comboBoxDevice.addItem(_fromUtf8(""))
        self.comboBoxDevice.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBoxDevice)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.checkboxOverwrite = QtGui.QCheckBox(self.groupBox_2)
        self.checkboxOverwrite.setObjectName(_fromUtf8("checkboxOverwrite"))
        self.verticalLayout_2.addWidget(self.checkboxOverwrite)
        self.checkboxOrient = QtGui.QCheckBox(self.groupBox_2)
        self.checkboxOrient.setObjectName(_fromUtf8("checkboxOrient"))
        self.verticalLayout_2.addWidget(self.checkboxOrient)
        self.checkboxResize = QtGui.QCheckBox(self.groupBox_2)
        self.checkboxResize.setObjectName(_fromUtf8("checkboxResize"))
        self.verticalLayout_2.addWidget(self.checkboxResize)
        self.checkboxQuantize = QtGui.QCheckBox(self.groupBox_2)
        self.checkboxQuantize.setObjectName(_fromUtf8("checkboxQuantize"))
        self.verticalLayout_2.addWidget(self.checkboxQuantize)
        self.checkboxFrame = QtGui.QCheckBox(self.groupBox_2)
        self.checkboxFrame.setObjectName(_fromUtf8("checkboxFrame"))
        self.verticalLayout_2.addWidget(self.checkboxFrame)
        self.checkboxSplit = QtGui.QCheckBox(self.groupBox_2)
        self.checkboxSplit.setObjectName(_fromUtf8("checkboxSplit"))
        self.verticalLayout_2.addWidget(self.checkboxSplit)
        self.checkboxReverse = QtGui.QCheckBox(self.groupBox_2)
        self.checkboxReverse.setObjectName(_fromUtf8("checkboxReverse"))
        self.verticalLayout_2.addWidget(self.checkboxReverse)
        self.checkboxCbz = QtGui.QCheckBox(self.groupBox_2)
        self.checkboxCbz.setObjectName(_fromUtf8("checkboxCbz"))
        self.verticalLayout_2.addWidget(self.checkboxCbz)
        self.checkboxCrop = QtGui.QCheckBox(self.groupBox_2)
        self.checkboxCrop.setObjectName(_fromUtf8("checkboxCrop"))
        self.verticalLayout_2.addWidget(self.checkboxCrop)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.thresholdSpinBox = QtGui.QDoubleSpinBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thresholdSpinBox.sizePolicy().hasHeightForWidth())
        self.thresholdSpinBox.setSizePolicy(sizePolicy)
        self.thresholdSpinBox.setMinimumSize(QtCore.QSize(55, 0))
        self.thresholdSpinBox.setDecimals(1)
        self.thresholdSpinBox.setMaximum(999.0)
        self.thresholdSpinBox.setProperty("value", 5.0)
        self.thresholdSpinBox.setObjectName(_fromUtf8("thresholdSpinBox"))
        self.horizontalLayout_2.addWidget(self.thresholdSpinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.checkboxCutNumbers = QtGui.QCheckBox(self.groupBox_2)
        self.checkboxCutNumbers.setEnabled(True)
        self.checkboxCutNumbers.setChecked(False)
        self.checkboxCutNumbers.setObjectName(_fromUtf8("checkboxCutNumbers"))
        self.verticalLayout_2.addWidget(self.checkboxCutNumbers)
        self.checkboxProgressBar = QtGui.QCheckBox(self.groupBox_2)
        self.checkboxProgressBar.setChecked(False)
        self.checkboxProgressBar.setObjectName(_fromUtf8("checkboxProgressBar"))
        self.verticalLayout_2.addWidget(self.checkboxProgressBar)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.spinboxProgressBar = QtGui.QSpinBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinboxProgressBar.sizePolicy().hasHeightForWidth())
        self.spinboxProgressBar.setSizePolicy(sizePolicy)
        self.spinboxProgressBar.setMinimumSize(QtCore.QSize(55, 0))
        self.spinboxProgressBar.setBaseSize(QtCore.QSize(0, 0))
        self.spinboxProgressBar.setMinimum(1)
        self.spinboxProgressBar.setProperty("value", 5)
        self.spinboxProgressBar.setObjectName(_fromUtf8("spinboxProgressBar"))
        self.horizontalLayout_4.addWidget(self.spinboxProgressBar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtGui.QSpacerItem(20, 1000, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 2, 1)
        self.gridLayout.setColumnStretch(1, 1)

        self.retranslateUi(DialogOptions)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogOptions.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogOptions.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogOptions)

    def retranslateUi(self, DialogOptions):
        DialogOptions.setWindowTitle(QtGui.QApplication.translate("DialogOptions", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogOptions", "Book", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogOptions", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("DialogOptions", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.prevOrig.setToolTip(QtGui.QApplication.translate("DialogOptions", "Before", None, QtGui.QApplication.UnicodeUTF8))
        self.prevPage1.setToolTip(QtGui.QApplication.translate("DialogOptions", "After: page 1", None, QtGui.QApplication.UnicodeUTF8))
        self.prevPage2.setToolTip(QtGui.QApplication.translate("DialogOptions", "After: page 2", None, QtGui.QApplication.UnicodeUTF8))
        self.prevPreviewButton.setText(QtGui.QApplication.translate("DialogOptions", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.nextPreviewButton.setText(QtGui.QApplication.translate("DialogOptions", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("DialogOptions", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogOptions", "Device", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDevice.setItemText(0, QtGui.QApplication.translate("DialogOptions", "Kindle 1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDevice.setItemText(1, QtGui.QApplication.translate("DialogOptions", "Kindle 2", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDevice.setItemText(2, QtGui.QApplication.translate("DialogOptions", "Kindle 3", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDevice.setItemText(3, QtGui.QApplication.translate("DialogOptions", "Kindle 4", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDevice.setItemText(4, QtGui.QApplication.translate("DialogOptions", "Kindle DX", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDevice.setItemText(5, QtGui.QApplication.translate("DialogOptions", "Kindle DXG", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxOverwrite.setText(QtGui.QApplication.translate("DialogOptions", "Overwrite existing files", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxOrient.setText(QtGui.QApplication.translate("DialogOptions", "Orient images to match aspect ratio", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxResize.setText(QtGui.QApplication.translate("DialogOptions", "Resize images to center on screen", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxQuantize.setText(QtGui.QApplication.translate("DialogOptions", "Dither images to match device palette", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxFrame.setText(QtGui.QApplication.translate("DialogOptions", "Draw frame around images", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxSplit.setText(QtGui.QApplication.translate("DialogOptions", "Split images to match aspect ratio", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxReverse.setText(QtGui.QApplication.translate("DialogOptions", "Reverse split order", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxCbz.setText(QtGui.QApplication.translate("DialogOptions", "Pack into CBZ file", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxCrop.setText(QtGui.QApplication.translate("DialogOptions", "Crop white space", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DialogOptions", "Crop threshold:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxCutNumbers.setText(QtGui.QApplication.translate("DialogOptions", "Cut page number at the bottom", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxProgressBar.setText(QtGui.QApplication.translate("DialogOptions", "Add progress bar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("DialogOptions", "on every n-th page:", None, QtGui.QApplication.UnicodeUTF8))

from mangle.imagecontainer import ImageContainer
import resources_rc
