# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dev/ui/book.ui'
#
# Created: Sat Jun 18 10:40:48 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindowBook(object):
    def setupUi(self, MainWindowBook):
        MainWindowBook.setObjectName(_fromUtf8("MainWindowBook"))
        MainWindowBook.resize(800, 600)
        MainWindowBook.setAcceptDrops(True)
        self.centralwidget = QtGui.QWidget(MainWindowBook)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.listWidgetFiles = QtGui.QListWidget(self.centralwidget)
        self.listWidgetFiles.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidgetFiles.setObjectName(_fromUtf8("listWidgetFiles"))
        self.horizontalLayout.addWidget(self.listWidgetFiles)
        MainWindowBook.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindowBook)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_Book = QtGui.QMenu(self.menubar)
        self.menu_Book.setObjectName(_fromUtf8("menu_Book"))
        self.menu_Add = QtGui.QMenu(self.menu_Book)
        self.menu_Add.setObjectName(_fromUtf8("menu_Add"))
        self.menu_Shift = QtGui.QMenu(self.menu_Book)
        self.menu_Shift.setObjectName(_fromUtf8("menu_Shift"))
        self.menuDownload = QtGui.QMenu(self.menu_Book)
        self.menuDownload.setObjectName(_fromUtf8("menuDownload"))
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName(_fromUtf8("menu_Help"))
        MainWindowBook.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MainWindowBook)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindowBook.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionFileNew = QtGui.QAction(MainWindowBook)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/file_new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFileNew.setIcon(icon)
        self.actionFileNew.setObjectName(_fromUtf8("actionFileNew"))
        self.actionFileOpen = QtGui.QAction(MainWindowBook)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/file_open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFileOpen.setIcon(icon1)
        self.actionFileOpen.setObjectName(_fromUtf8("actionFileOpen"))
        self.actionFileSave = QtGui.QAction(MainWindowBook)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/save_file.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFileSave.setIcon(icon2)
        self.actionFileSave.setObjectName(_fromUtf8("actionFileSave"))
        self.actionFileSaveAs = QtGui.QAction(MainWindowBook)
        self.actionFileSaveAs.setObjectName(_fromUtf8("actionFileSaveAs"))
        self.actionFileExit = QtGui.QAction(MainWindowBook)
        self.actionFileExit.setObjectName(_fromUtf8("actionFileExit"))
        self.actionBookOptions = QtGui.QAction(MainWindowBook)
        self.actionBookOptions.setObjectName(_fromUtf8("actionBookOptions"))
        self.actionBookRemove = QtGui.QAction(MainWindowBook)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/remove_files.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBookRemove.setIcon(icon3)
        self.actionBookRemove.setObjectName(_fromUtf8("actionBookRemove"))
        self.actionBookExport = QtGui.QAction(MainWindowBook)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/export_book.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBookExport.setIcon(icon4)
        self.actionBookExport.setObjectName(_fromUtf8("actionBookExport"))
        self.actionHelpHomepage = QtGui.QAction(MainWindowBook)
        self.actionHelpHomepage.setObjectName(_fromUtf8("actionHelpHomepage"))
        self.actionHelpAbout = QtGui.QAction(MainWindowBook)
        self.actionHelpAbout.setObjectName(_fromUtf8("actionHelpAbout"))
        self.actionBookAddFiles = QtGui.QAction(MainWindowBook)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/add_file.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBookAddFiles.setIcon(icon5)
        self.actionBookAddFiles.setObjectName(_fromUtf8("actionBookAddFiles"))
        self.actionBookAddDirectory = QtGui.QAction(MainWindowBook)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/add_directory.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBookAddDirectory.setIcon(icon6)
        self.actionBookAddDirectory.setObjectName(_fromUtf8("actionBookAddDirectory"))
        self.actionBookShiftUp = QtGui.QAction(MainWindowBook)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/shift_up.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBookShiftUp.setIcon(icon7)
        self.actionBookShiftUp.setObjectName(_fromUtf8("actionBookShiftUp"))
        self.actionBookShiftDown = QtGui.QAction(MainWindowBook)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/shift_down.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBookShiftDown.setIcon(icon8)
        self.actionBookShiftDown.setObjectName(_fromUtf8("actionBookShiftDown"))
        self.actionReadmanga = QtGui.QAction(MainWindowBook)
        self.actionReadmanga.setObjectName(_fromUtf8("actionReadmanga"))
        self.actionAdultmanga = QtGui.QAction(MainWindowBook)
        self.actionAdultmanga.setObjectName(_fromUtf8("actionAdultmanga"))
        self.menu_File.addAction(self.actionFileNew)
        self.menu_File.addAction(self.actionFileOpen)
        self.menu_File.addAction(self.actionFileSave)
        self.menu_File.addAction(self.actionFileSaveAs)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionFileExit)
        self.menu_Add.addAction(self.actionBookAddFiles)
        self.menu_Add.addAction(self.actionBookAddDirectory)
        self.menu_Shift.addAction(self.actionBookShiftUp)
        self.menu_Shift.addAction(self.actionBookShiftDown)
        self.menuDownload.addAction(self.actionReadmanga)
        self.menuDownload.addAction(self.actionAdultmanga)
        self.menu_Book.addAction(self.actionBookOptions)
        self.menu_Book.addSeparator()
        self.menu_Book.addAction(self.menu_Add.menuAction())
        self.menu_Book.addAction(self.actionBookRemove)
        self.menu_Book.addAction(self.menu_Shift.menuAction())
        self.menu_Book.addSeparator()
        self.menu_Book.addAction(self.actionBookExport)
        self.menu_Book.addSeparator()
        self.menu_Book.addAction(self.menuDownload.menuAction())
        self.menu_Help.addAction(self.actionHelpHomepage)
        self.menu_Help.addAction(self.actionHelpAbout)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Book.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar.addAction(self.actionFileNew)
        self.toolBar.addAction(self.actionFileOpen)
        self.toolBar.addAction(self.actionFileSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionBookAddFiles)
        self.toolBar.addAction(self.actionBookAddDirectory)
        self.toolBar.addAction(self.actionBookRemove)
        self.toolBar.addAction(self.actionBookShiftUp)
        self.toolBar.addAction(self.actionBookShiftDown)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionBookExport)

        self.retranslateUi(MainWindowBook)
        QtCore.QObject.connect(self.actionFileExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindowBook.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindowBook)

    def retranslateUi(self, MainWindowBook):
        MainWindowBook.setWindowTitle(QtGui.QApplication.translate("MainWindowBook", "Mangle", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindowBook", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Book.setTitle(QtGui.QApplication.translate("MainWindowBook", "&Book", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Add.setTitle(QtGui.QApplication.translate("MainWindowBook", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Shift.setTitle(QtGui.QApplication.translate("MainWindowBook", "&Shift", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDownload.setTitle(QtGui.QApplication.translate("MainWindowBook", "Download from", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindowBook", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindowBook", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFileNew.setText(QtGui.QApplication.translate("MainWindowBook", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFileNew.setToolTip(QtGui.QApplication.translate("MainWindowBook", "New book", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFileNew.setShortcut(QtGui.QApplication.translate("MainWindowBook", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFileOpen.setText(QtGui.QApplication.translate("MainWindowBook", "&Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFileOpen.setToolTip(QtGui.QApplication.translate("MainWindowBook", "Open book", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFileOpen.setShortcut(QtGui.QApplication.translate("MainWindowBook", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFileSave.setText(QtGui.QApplication.translate("MainWindowBook", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFileSave.setToolTip(QtGui.QApplication.translate("MainWindowBook", "Save book", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFileSave.setShortcut(QtGui.QApplication.translate("MainWindowBook", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFileSaveAs.setText(QtGui.QApplication.translate("MainWindowBook", "Save &as...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFileSaveAs.setToolTip(QtGui.QApplication.translate("MainWindowBook", "Save book as", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFileSaveAs.setShortcut(QtGui.QApplication.translate("MainWindowBook", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFileExit.setText(QtGui.QApplication.translate("MainWindowBook", "&Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFileExit.setShortcut(QtGui.QApplication.translate("MainWindowBook", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBookOptions.setText(QtGui.QApplication.translate("MainWindowBook", "&Options...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBookRemove.setText(QtGui.QApplication.translate("MainWindowBook", "&Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBookRemove.setToolTip(QtGui.QApplication.translate("MainWindowBook", "Remove files", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBookRemove.setShortcut(QtGui.QApplication.translate("MainWindowBook", "Del", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBookExport.setText(QtGui.QApplication.translate("MainWindowBook", "&Export...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBookExport.setToolTip(QtGui.QApplication.translate("MainWindowBook", "Export book", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBookExport.setShortcut(QtGui.QApplication.translate("MainWindowBook", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelpHomepage.setText(QtGui.QApplication.translate("MainWindowBook", "&Homepage...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelpAbout.setText(QtGui.QApplication.translate("MainWindowBook", "&About...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelpAbout.setToolTip(QtGui.QApplication.translate("MainWindowBook", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelpAbout.setShortcut(QtGui.QApplication.translate("MainWindowBook", "F1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBookAddFiles.setText(QtGui.QApplication.translate("MainWindowBook", "&Files...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBookAddFiles.setToolTip(QtGui.QApplication.translate("MainWindowBook", "Add files", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBookAddFiles.setShortcut(QtGui.QApplication.translate("MainWindowBook", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBookAddDirectory.setText(QtGui.QApplication.translate("MainWindowBook", "&Directory...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBookAddDirectory.setToolTip(QtGui.QApplication.translate("MainWindowBook", "Add directory", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBookAddDirectory.setShortcut(QtGui.QApplication.translate("MainWindowBook", "Ctrl+D", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBookShiftUp.setText(QtGui.QApplication.translate("MainWindowBook", "&Up", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBookShiftUp.setToolTip(QtGui.QApplication.translate("MainWindowBook", "Shift files up", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBookShiftUp.setShortcut(QtGui.QApplication.translate("MainWindowBook", "Ctrl+PgUp", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBookShiftDown.setText(QtGui.QApplication.translate("MainWindowBook", "&Down", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBookShiftDown.setToolTip(QtGui.QApplication.translate("MainWindowBook", "Shift files down", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBookShiftDown.setShortcut(QtGui.QApplication.translate("MainWindowBook", "Ctrl+PgDown", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReadmanga.setText(QtGui.QApplication.translate("MainWindowBook", "readmanga.ru", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdultmanga.setText(QtGui.QApplication.translate("MainWindowBook", "adultmanga.ru", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
