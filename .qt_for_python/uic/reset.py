# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reset.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from windowdragger import WindowDragger


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 500)
        icon = QIcon()
        icon.addFile(u"../images/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QProgressBar:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    text-align: center;\n"
"    padding: 1px;\n"
"    background: #201F1F;\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.545, x2:1, y2:0, stop:0 rgba(28, 66, 111, 255), stop:1 rgba(37, 87, 146, 255));\n"
"}\n"
"\n"
"QToolTip\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 1px;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: silver;\n"
"    background-color: #302F2F;\n"
"    selection-background-color:#3d8ec9;\n"
"    selection-color: black;\n"
"    background-clip: border;\n"
"    border-image: none;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: #78879b;\n"
"    color: black;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: #3d8ec9;\n"
"}\n"
"\n"
"QCheckBox {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QRadioButton\n"
"{\n"
""
                        "    spacing: 5px;\n"
"    outline: none;\n"
"    color: #bbb;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"QRadioButton:disabled\n"
"{\n"
"    color: #777777;\n"
"}\n"
"QRadioButton::indicator\n"
"{\n"
"    width: 21px;\n"
"    height: 21px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked,\n"
"QRadioButton::indicator:unchecked:hover\n"
"{\n"
"    image: url(:/dark_blue/img/radio_unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:focus,\n"
"QRadioButton::indicator:unchecked:pressed\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/dark_blue/img/radio_unchecked_focus.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked,\n"
"QRadioButton::indicator:checked:hover\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/dark_blue/img/radio_checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:focus,\n"
"QRadioButton::indicato::menu-arrowr:checked:pressed\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/dark_blue/img/radio_checked_focus.png);\n"
"}\n"
""
                        "\n"
"QRadioButton::indicator:indeterminate,\n"
"QRadioButton::indicator:indeterminate:hover,\n"
"QRadioButton::indicator:indeterminate:pressed\n"
"{\n"
"        image: url(:/dark_blue/img/radio_indeterminate.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:disabled\n"
"{\n"
"  outline: none;\n"
"  image: url(:/dark_blue/img/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:disabled\n"
"{\n"
"    image: url(:/dark_blue/img/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"\n"
"QMenuBar\n"
"{\n"
"    background-color: #302F2F;\n"
"    color: silver;\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    background-color: #3d8ec9;\n"
"    color: black;\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"   "
                        " color: silver;\n"
"    margin: 1px;\n"
"}\n"
"\n"
"QMenu::icon\n"
"{\n"
"    margin: 1px;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 2px 2px 25px;\n"
"    margin-left: 5px;\n"
"    border: 1px solid transparent; /* reserve space for selection border */\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: black;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 2px;\n"
"    background: lightblue;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"/* non-exclusive indicator = check box style indicator\n"
"   (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:non-exclusive:unchecked {\n"
"    image: url(:/dark_blue/img/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:selected {\n"
"    image: url(:/dark_blue/img/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked {\n"
"    image: url(:/dark_blue/img/checkbox_checked.png);\n"
"}\n"
""
                        "\n"
"QMenu::indicator:non-exclusive:checked:selected {\n"
"    image: url(:/dark_blue/img/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"/* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:exclusive:unchecked {\n"
"    image: url(:/dark_blue/img/radio_unchecked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:selected {\n"
"    image: url(:/dark_blue/img/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked {\n"
"    image: url(:/dark_blue/img/radio_checked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:selected {\n"
"    image: url(:/dark_blue/img/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QMenu::right-arrow {\n"
"    margin: 5px;\n"
"    image: url(:/dark_blue/img/right_arrow.png)\n"
"}\n"
"\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #808080;\n"
"    background-color: #302F2F;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    alternate-background-color: #3A3939;\n"
"    color: silver;\n"
"    border: 1px"
                        " solid 3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QWidget:focus, QMenuBar:focus\n"
"{\n"
"    border: 1px solid #78879b;\n"
"}\n"
"\n"
"QTabWidget:focus, QCheckBox:focus, QRadioButton:focus, QSlider:focus\n"
"{\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: #201F1F;\n"
"    padding: 2px;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    color: silver;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border:1px solid #787878;\n"
"    border-radius: 10px;\n"
"    margin-top: 20px;\n"
"	background-color : transparent;\n"
"    color: silver;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"QAbstractScrollArea\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"   "
                        " height: 15px;\n"
"    margin: 3px 15px 3px 15px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"    background-color: #2A2929;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-width: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/dark_blue/img/right_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/dark_blue/img/left_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"{\n"
"    border-image: url(:/dark_blue/img/right_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
""
                        "    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"{\n"
"    border-image: url(:/dark_blue/img/left_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #2A2929;\n"
"    width: 15px;\n"
"    margin: 15px 3px 15px 3px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-height: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/dark_"
                        "blue/img/up_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/dark_blue/img/down_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    border-image: url(:/dark_blue/img/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/dark_blue/img/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
""
                        "{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #201F1F;\n"
"    color: silver;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #201F1F;;\n"
"    color: silver;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QSizeGrip {\n"
"    image: url(:/dark_blue/img/sizegrip.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QMainWindow\n"
"{\n"
"    background-color: #302F2F;\n"
"\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: #302F2F;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    spacing: 2px;\n"
"    border: 1px dashed #3A3939;\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"  "
                        "  background-color: #787876;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #3A3939;\n"
"    spacing: 2px;\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 1px;\n"
"    background-color: #3A3939;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"\n"
"QFrame\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"QFrame[frameShape=\"0\"]\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px transparent #444;\n"
"}\n"
"\n"
"QStackedWidget\n"
"{\n"
"    background-color: #302F2F;\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QToolBar {\n"
"    border: 1px transparent #393838;\n"
"    background: 1px solid #302F2F;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal {\n"
"    image: url(:/dark_blue/img/Hmovetoolbar.png);\n"
"}\n"
"QToolBar::handle:vertical {\n"
"    image: url(:/dark_blue/img/Vmovetoolbar.png);\n"
"}\n"
"QToolBar::separator:horizontal {\n"
"  "
                        "  image: url(:/dark_blue/img/Hsepartoolbar.png);\n"
"}\n"
"QToolBar::separator:vertical {\n"
"    image: url(:/dark_blue/img/Vsepartoolbars.png);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: silver;\n"
"    background-color: #302F2F;\n"
"    border-width: 2px;\n"
"    border-color: #4A4949;\n"
"    border-style: solid;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    border-radius: 4px;\n"
"    /* outline: none; */\n"
"    /* min-width: 40px; */\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #302F2F;\n"
"    border-width: 2px;\n"
"    border-color: #3A3939;\n"
"    border-style: solid;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    /*border-radius: 2px;*/\n"
"    color: #808080;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #3d8ec9;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #3d8ec9;\n"
""
                        "    background-color: #201F1F;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 2px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: #4A4949;\n"
"    border-color: #6A6969;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QComboBox:hover, QAbstractSpinBox:hover,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QAbstractView:hover,QTreeView:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #626873;\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    selection-background-color: #4a4a4a;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #201F1F;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #444;\n"
"    selection-background-color: #3d8ec9;\n"
"    color: silver;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padd"
                        "ing;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow_disabled.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on, QComboBox::down-arrow:hover,\n"
"QComboBox::down-arrow:focus\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #484846;\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: #201F1F;\n"
"    color: silver;\n"
"    border-radius: 2px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"}\n"
"\n"
"QAbstractSpinBox:dow"
                        "n-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow,QAbstractSpinBox::up-arrow:disabled,QAbstractSpinBox::up-arrow:off {\n"
"    image: url(:/dark_blue/img/up_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::up-arrow:hover\n"
"{\n"
"    image: url(:/dark_blue/img/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QAbstractSpinBox::down-arrow,QAbstractSpinBox::down-arrow:disabled,QAbstractSpinBox::down-arrow:off\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::down-arrow:hover\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"\n"
"QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"}\n"
"\n"
"QTabWidget{\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
""
                        "}\n"
"\n"
"QTabBar\n"
"{\n"
"    qproperty-drawBase: 0;\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"QTabBar:focus\n"
"{\n"
"    border: 0px transparent black;\n"
"}\n"
"\n"
"QTabBar::close-button  {\n"
"    image: url(:/dark_blue/img/close.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:hover\n"
"{\n"
"    image: url(:/dark_blue/img/close-hover.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:pressed {\n"
"    image: url(:/dark_blue/img/close-pressed.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* TOP TABS */\n"
"QTabBar::tab:top {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-bottom: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-bo"
                        "ttom: 1px transparent #4A4949;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"/* BOTTOM TABS */\n"
"QTabBar::tab:bottom {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-top: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-bottom-left-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-top: 1px transparent #4A4949;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:hover {\n"
"    background-color: #78879b;\n"
"}\n"
"\n"
"/* LEFT TABS */\n"
"QTabBar::tab:left {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-left: 1px transparent black;\n"
"    back"
                        "ground-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-right-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-right: 1px transparent #4A4949;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"\n"
"/* RIGHT TABS */\n"
"QTabBar::tab:right {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-right: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 2px;\n"
"    border-bottom-left-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-right: 1px transparent #4A4949;\n"
"    border-top-left-radius: 0px;\n"
"  "
                        "  border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled {\n"
"     image: url(:/dark_blue/img/right_arrow.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:enabled {\n"
"     image: url(:/dark_blue/img/left_arrow.png);\n"
" }\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled {\n"
"     image: url(:/dark_blue/img/right_arrow_disabled.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:disabled {\n"
"     image: url(:/dark_blue/img/left_arrow_disabled.png);\n"
" }\n"
"\n"
"\n"
"QDockWidget {\n"
"    border: 1px solid #403F3F;\n"
"    titlebar-close-icon: url(:/dark_blue/img/close.png);\n"
"    titlebar-normal-icon: url(:/dark_blue/img/undock.png);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 2px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-butt"
                        "on:hover {\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {\n"
"    padding: 1px -1px -1px 1px;\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QTreeView, QListView, QTextBrowser, AtLineEdit, AtLineEdit::hover {\n"
"    border: 1px solid #444;\n"
"    background-color: silver;\n"
"    border-radius: 3px;\n"
"    margin-left: 3px;\n"
"    color: black;\n"
"}\n"
"\n"
"QTreeView:branch:selected, QTreeView:branch:hover {\n"
"    background: url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"    border-image: url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"    border-image: url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"    border-image: url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"Q"
                        "TreeView::branch:closed:has-children:has-siblings {\n"
"    image: url(:/dark_blue/img/branch_closed.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  {\n"
"    image: url(:/dark_blue/img/branch_open.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed:hover,\n"
"QTreeView::branch:closed:has-children:has-siblings:hover {\n"
"    image: url(:/dark_blue/img/branch_closed-on.png);\n"
"    }\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings:hover,\n"
"QTreeView::branch:open:has-children:has-siblings:hover  {\n"
"    image: url(:/dark_blue/img/branch_open-on.png);\n"
"    }\n"
"\n"
"QListView::item:!selected:hover, QListView::item:!selected:hover, QTreeView::item:!selected:hover  {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    outline: 0;\n"
"    color: #FFFFFF\n"
"}\n"
"\n"
"QListView::item:selected:hover, QListView::item:selected:hover, QTreeView::item:selected:hover  {\n"
"    background: #3d8ec9;\n"
"    col"
                        "or: #FFFFFF;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    height: 8px;\n"
"    background: #201F1F;\n"
"    margin: 2px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: -4px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid #3A3939;\n"
"    width: 8px;\n"
"    background: #201F1F;\n"
"    margin: 0 0px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,\n"
"    stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: 0 -4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QToolButton {\n"
"    /*  background"
                        "-color: transparent; */\n"
"    border: 2px transparent #4A4949;\n"
"    border-radius: 4px;\n"
"    background-color: dimgray;\n"
"    margin: 2px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
" padding-right: 20px; /* make way for the popup button */\n"
" border: 2px transparent #4A4949;\n"
" border-radius: 4px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"2\"] { /* only for InstantPopup */\n"
" padding-right: 10px; /* make way for the popup button */\n"
" border: 2px transparent #4A4949;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover, QToolButton::menu-button:hover {\n"
"    border: 2px solid #78879b;\n"
"}\n"
"\n"
"QToolButton:checked, QToolButton:pressed,\n"
"    QToolButton::menu-button:pressed {\n"
"    background-color: #4A4949;\n"
"    border: 2px solid #78879b;\n"
"}\n"
"\n"
"/* the subcontrol below is used only in the InstantPopup or DelayedPopup mode */\n"
"QToolButton::menu-indicator {\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"    top: -7px; "
                        "left: -2px; /* shift it a bit */\n"
"}\n"
"\n"
"/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
"QToolButton::menu-button {\n"
"    border: 1px transparent #4A4949;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    /* 16px width + 4px for border = 20px allocated above */\n"
"    width: 16px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"QToolButton::menu-arrow:open {\n"
"    top: 1px; left: 1px; /* shift it a bit */\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QPushButton::menu-indicator  {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"    left: 4px;\n"
"}\n"
"\n"
"QTableView\n"
"{\n"
"    border: 1px solid #444;\n"
"    gridline-color: #6c6c6c;\n"
"    background-color: #201F1F;\n"
"}\n"
"\n"
"\n"
"QTableView, QHeaderView\n"
"{\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QTableView::item:pressed, QListView::item:pressed, QTr"
                        "eeView::item:pressed  {\n"
"    background: #78879b;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QTableView::item:selected:active, QTreeView::item:selected:active, QListView::item:selected:active  {\n"
"    background: #3d8ec9;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"\n"
"QHeaderView\n"
"{\n"
"    border: 1px transparent;\n"
"    border-radius: 2px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QHeaderView::section  {\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QHeaderView::section::vertical::first, QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: transparent;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
""
                        "    border-left: transparent;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
" {\n"
"    color: white;\n"
"    background-color: #5A5959;\n"
" }\n"
"\n"
" /* style the sort indicator */\n"
"QHeaderView::down-arrow {\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"    image: url(:/dark_blue/img/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #3A3939;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QToolBox  {\n"
"    padding: 3px;\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"    color: #b1b1b1;\n"
"    background-color: #302F2F;\n"
"    border: 1px solid #4A4949;\n"
"    border-bottom: 1px transparent #302F2F;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"\n"
" QToolBox::tab:selected { /* italicize selected tabs */\n"
"    font: italic;\n"
"    background-color: #302F2F;\n"
"    border-color: #3d8ec9;\n"
" }\n"
"\n"
"QSta"
                        "tusBar::item {\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
" }\n"
"\n"
"\n"
"QFrame[height=\"3\"], QFrame[width=\"3\"] {\n"
"    background-color: #AAA;\n"
"}\n"
"\n"
"\n"
"QSplitter::handle {\n"
"    border: 1px dashed #3A3939;\n"
"}\n"
"\n"
"QSplitter::handle:hover {\n"
"    background-color: #787876;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    width: 1px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"    height: 1px;\n"
"}\n"
"\n"
"QListWidget {\n"
"    background-color: silver;\n"
"    border-radius: 5px;\n"
"    margin-left: 5px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    color: black;\n"
"}\n"
"\n"
"QMessageBox {\n"
"    messagebox-critical-icon	: url(:/dark_blue/img/critical.png);\n"
"    messagebox-information-icon	: url(:/dark_blue/img/information.png);\n"
"    messagebox-question-icon	: url(:/dark_blue/img/question.png);\n"
"    messagebox-warning-icon:    : url(:/dark_blue/img/warning.png);\n"
"}\n"
"\n"
"ColorButton::enabled {\n"
""
                        "    border-radius: 0px;\n"
"    border: 1px solid #444444;\n"
"}\n"
"\n"
"ColorButton::disabled {\n"
"    border-radius: 0px;\n"
"    border: 1px solid #AAAAAA;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.back = QLabel(self.centralwidget)
        self.back.setObjectName(u"back")
        self.back.setEnabled(True)
        self.back.setGeometry(QRect(0, 0, 800, 500))
        self.back.setScaledContents(True)
        self.back.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox1 = QGroupBox(self.centralwidget)
        self.groupBox1.setObjectName(u"groupBox1")
        self.groupBox1.setGeometry(QRect(40, 50, 330, 420))
        font = QFont()
        font.setPointSize(9)
        self.groupBox1.setFont(font)
        self.groupBox1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox1.setFlat(False)
        self.groupBox1.setCheckable(False)
        self.label1 = QLabel(self.groupBox1)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(20, 44, 140, 16))
        self.label1.setFont(font)
        self.label1.setStyleSheet(u"background-color:transparent;\n"
"")
        self.attach_btn1 = QPushButton(self.groupBox1)
        self.attach_btn1.setObjectName(u"attach_btn1")
        self.attach_btn1.setGeometry(QRect(210, 40, 100, 24))
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setWeight(75)
        self.attach_btn1.setFont(font1)
        self.attach_btn1.setStyleSheet(u"QPushButton{background-color:rgba(57,167,23,220);color:white;border:0px;}\n"
"QPushButton:hover{background-color:rgba(57,167,23,255);color:white;}\n"
"QPushButton:pressed{background-color:rgba(57,167,23,235);}")
        self.label2 = QLabel(self.groupBox1)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(20, 74, 151, 16))
        self.label2.setFont(font)
        self.label2.setStyleSheet(u"background-color:transparent;\n"
"")
        self.attach_btn2 = QPushButton(self.groupBox1)
        self.attach_btn2.setObjectName(u"attach_btn2")
        self.attach_btn2.setGeometry(QRect(210, 70, 100, 24))
        self.attach_btn2.setFont(font1)
        self.attach_btn2.setStyleSheet(u"QPushButton{background-color:rgba(57,167,23,220);color:white;border:0px;}\n"
"QPushButton:hover{background-color:rgba(57,167,23,255);color:white;}\n"
"QPushButton:pressed{background-color:rgba(57,167,23,235);}")
        self.label3 = QLabel(self.groupBox1)
        self.label3.setObjectName(u"label3")
        self.label3.setGeometry(QRect(20, 104, 171, 16))
        self.label3.setFont(font)
        self.label3.setStyleSheet(u"background-color:transparent;\n"
"")
        self.attach_btn3 = QPushButton(self.groupBox1)
        self.attach_btn3.setObjectName(u"attach_btn3")
        self.attach_btn3.setEnabled(True)
        self.attach_btn3.setGeometry(QRect(210, 100, 100, 24))
        self.attach_btn3.setFont(font1)
        self.attach_btn3.setStyleSheet(u"QPushButton{background-color:rgba(57,167,23,220);color:white;border:0px;}\n"
"QPushButton:hover{background-color:rgba(57,167,23,255);color:white;}\n"
"QPushButton:pressed{background-color:rgba(57,167,23,235);}")
        self.label4 = QLabel(self.groupBox1)
        self.label4.setObjectName(u"label4")
        self.label4.setGeometry(QRect(20, 134, 140, 16))
        self.label4.setFont(font)
        self.label4.setStyleSheet(u"background-color:transparent;\n"
"")
        self.attach_btn4 = QPushButton(self.groupBox1)
        self.attach_btn4.setObjectName(u"attach_btn4")
        self.attach_btn4.setGeometry(QRect(210, 130, 100, 24))
        self.attach_btn4.setFont(font1)
        self.attach_btn4.setStyleSheet(u"QPushButton{background-color:rgba(57,167,23,220);color:white;border:0px;}\n"
"QPushButton:hover{background-color:rgba(57,167,23,255);color:white;}\n"
"QPushButton:pressed{background-color:rgba(57,167,23,235);}")
        self.label5 = QLabel(self.groupBox1)
        self.label5.setObjectName(u"label5")
        self.label5.setGeometry(QRect(20, 164, 171, 16))
        self.label5.setFont(font)
        self.label5.setStyleSheet(u"background-color:transparent;\n"
"")
        self.attach_btn5 = QPushButton(self.groupBox1)
        self.attach_btn5.setObjectName(u"attach_btn5")
        self.attach_btn5.setGeometry(QRect(210, 160, 100, 24))
        self.attach_btn5.setFont(font1)
        self.attach_btn5.setStyleSheet(u"QPushButton{background-color:rgba(57,167,23,220);color:white;border:0px;}\n"
"QPushButton:hover{background-color:rgba(57,167,23,255);color:white;}\n"
"QPushButton:pressed{background-color:rgba(57,167,23,235);}")
        self.label6 = QLabel(self.groupBox1)
        self.label6.setObjectName(u"label6")
        self.label6.setGeometry(QRect(20, 194, 161, 16))
        self.label6.setFont(font)
        self.label6.setStyleSheet(u"background-color:transparent;\n"
"")
        self.attach_btn6 = QPushButton(self.groupBox1)
        self.attach_btn6.setObjectName(u"attach_btn6")
        self.attach_btn6.setGeometry(QRect(210, 190, 100, 24))
        self.attach_btn6.setFont(font1)
        self.attach_btn6.setStyleSheet(u"QPushButton{background-color:rgba(57,167,23,220);color:white;border:0px;}\n"
"QPushButton:hover{background-color:rgba(57,167,23,255);color:white;}\n"
"QPushButton:pressed{background-color:rgba(57,167,23,235);}")
        self.label7 = QLabel(self.groupBox1)
        self.label7.setObjectName(u"label7")
        self.label7.setGeometry(QRect(20, 224, 171, 16))
        self.label7.setFont(font)
        self.label7.setStyleSheet(u"background-color:transparent;\n"
"")
        self.attach_btn12 = QPushButton(self.groupBox1)
        self.attach_btn12.setObjectName(u"attach_btn12")
        self.attach_btn12.setGeometry(QRect(210, 370, 100, 24))
        self.attach_btn12.setFont(font1)
        self.attach_btn12.setStyleSheet(u"QPushButton{background-color:rgba(57,167,23,220);color:white;border:0px;}\n"
"QPushButton:hover{background-color:rgba(57,167,23,255);color:white;}\n"
"QPushButton:pressed{background-color:rgba(57,167,23,235);}")
        self.label12 = QLabel(self.groupBox1)
        self.label12.setObjectName(u"label12")
        self.label12.setGeometry(QRect(20, 374, 140, 16))
        self.label12.setFont(font)
        self.label12.setStyleSheet(u"background-color:transparent;\n"
"")
        self.attach_btn11 = QPushButton(self.groupBox1)
        self.attach_btn11.setObjectName(u"attach_btn11")
        self.attach_btn11.setGeometry(QRect(210, 340, 100, 24))
        self.attach_btn11.setFont(font1)
        self.attach_btn11.setStyleSheet(u"QPushButton{background-color:rgba(57,167,23,220);color:white;border:0px;}\n"
"QPushButton:hover{background-color:rgba(57,167,23,255);color:white;}\n"
"QPushButton:pressed{background-color:rgba(57,167,23,235);}")
        self.label9 = QLabel(self.groupBox1)
        self.label9.setObjectName(u"label9")
        self.label9.setGeometry(QRect(20, 284, 140, 16))
        self.label9.setFont(font)
        self.label9.setStyleSheet(u"background-color:transparent;\n"
"")
        self.label8 = QLabel(self.groupBox1)
        self.label8.setObjectName(u"label8")
        self.label8.setGeometry(QRect(20, 254, 161, 16))
        self.label8.setFont(font)
        self.label8.setStyleSheet(u"background-color:transparent;\n"
"")
        self.label11 = QLabel(self.groupBox1)
        self.label11.setObjectName(u"label11")
        self.label11.setGeometry(QRect(20, 344, 151, 16))
        self.label11.setFont(font)
        self.label11.setStyleSheet(u"background-color:transparent;\n"
"")
        self.attach_btn10 = QPushButton(self.groupBox1)
        self.attach_btn10.setObjectName(u"attach_btn10")
        self.attach_btn10.setGeometry(QRect(210, 310, 100, 24))
        self.attach_btn10.setFont(font1)
        self.attach_btn10.setStyleSheet(u"QPushButton{background-color:rgba(57,167,23,220);color:white;border:0px;}\n"
"QPushButton:hover{background-color:rgba(57,167,23,255);color:white;}\n"
"QPushButton:pressed{background-color:rgba(57,167,23,235);}")
        self.label10 = QLabel(self.groupBox1)
        self.label10.setObjectName(u"label10")
        self.label10.setGeometry(QRect(20, 314, 161, 16))
        self.label10.setFont(font)
        self.label10.setStyleSheet(u"background-color:transparent;\n"
"")
        self.attach_btn9 = QPushButton(self.groupBox1)
        self.attach_btn9.setObjectName(u"attach_btn9")
        self.attach_btn9.setGeometry(QRect(210, 280, 100, 24))
        self.attach_btn9.setFont(font1)
        self.attach_btn9.setStyleSheet(u"QPushButton{background-color:rgba(57,167,23,220);color:white;border:0px;}\n"
"QPushButton:hover{background-color:rgba(57,167,23,255);color:white;}\n"
"QPushButton:pressed{background-color:rgba(57,167,23,235);}")
        self.attach_btn7 = QPushButton(self.groupBox1)
        self.attach_btn7.setObjectName(u"attach_btn7")
        self.attach_btn7.setGeometry(QRect(210, 220, 100, 24))
        self.attach_btn7.setFont(font1)
        self.attach_btn7.setStyleSheet(u"QPushButton{background-color:rgba(57,167,23,220);color:white;border:0px;}\n"
"QPushButton:hover{background-color:rgba(57,167,23,255);color:white;}\n"
"QPushButton:pressed{background-color:rgba(57,167,23,235);}")
        self.attach_btn8 = QPushButton(self.groupBox1)
        self.attach_btn8.setObjectName(u"attach_btn8")
        self.attach_btn8.setGeometry(QRect(210, 250, 100, 24))
        self.attach_btn8.setFont(font1)
        self.attach_btn8.setStyleSheet(u"QPushButton{background-color:rgba(57,167,23,220);color:white;border:0px;}\n"
"QPushButton:hover{background-color:rgba(57,167,23,255);color:white;}\n"
"QPushButton:pressed{background-color:rgba(57,167,23,235);}")
        self.windowTitlebar = WindowDragger(self.centralwidget)
        self.windowTitlebar.setObjectName(u"windowTitlebar")
        self.windowTitlebar.setGeometry(QRect(0, 3, 804, 27))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.windowTitlebar.sizePolicy().hasHeightForWidth())
        self.windowTitlebar.setSizePolicy(sizePolicy)
        self.windowTitlebar.setMaximumSize(QSize(16777215, 27))
        self.windowTitlebar.setStyleSheet(u"background-color: transparent;")
        self.horizontalLayout = QHBoxLayout(self.windowTitlebar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 5, 0)
        self.iconLabel = QLabel(self.windowTitlebar)
        self.iconLabel.setObjectName(u"iconLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.iconLabel.sizePolicy().hasHeightForWidth())
        self.iconLabel.setSizePolicy(sizePolicy1)
        self.iconLabel.setMinimumSize(QSize(23, 23))
        self.iconLabel.setMaximumSize(QSize(23, 23))
        self.iconLabel.setScaledContents(True)

        self.horizontalLayout.addWidget(self.iconLabel)

        self.titleLabel = QLabel(self.windowTitlebar)
        self.titleLabel.setObjectName(u"titleLabel")
        font2 = QFont()
        font2.setPointSize(10)
        self.titleLabel.setFont(font2)
        self.titleLabel.setStyleSheet(u"color:white;")

        self.horizontalLayout.addWidget(self.titleLabel)

        self.btnMinimize = QToolButton(self.windowTitlebar)
        self.btnMinimize.setObjectName(u"btnMinimize")
        self.btnMinimize.setStyleSheet(u"#btnMinimize\n"
"{\n"
"     background-color:none;\n"
"     border:none;\n"
"     width:16px;\n"
"     height:16px;\n"
"     padding:4px;\n"
" }\n"
"#btnMinimize:hover\n"
"{\n"
"     background-color:rgb(127, 127, 127);\n"
" }\n"
"#btnMinimize:pressed\n"
"{\n"
"     background-color:rgb(0, 120, 215);\n"
" }")

        self.horizontalLayout.addWidget(self.btnMinimize)

        self.btnClose = QToolButton(self.windowTitlebar)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setStyleSheet(u"#btnClose\n"
"{\n"
"     background-color:none;\n"
"     border:none;\n"
"     width:16px;\n"
"     height:16px;\n"
"     padding:4px;\n"
" }\n"
"#btnClose:hover\n"
"{\n"
"     background-color:rgb(127, 127, 127);\n"
" }\n"
"#btnClose:pressed\n"
"{\n"
"     background-color:rgb(0, 120, 215);\n"
" }")

        self.horizontalLayout.addWidget(self.btnClose)

        self.horizontalLayout.setStretch(1, 1)
        self.groupBox2 = QGroupBox(self.centralwidget)
        self.groupBox2.setObjectName(u"groupBox2")
        self.groupBox2.setGeometry(QRect(430, 50, 330, 420))
        self.groupBox2.setFont(font)
        self.groupBox2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox2.setFlat(False)
        self.groupBox2.setCheckable(False)
        self.label13 = QLabel(self.groupBox2)
        self.label13.setObjectName(u"label13")
        self.label13.setGeometry(QRect(20, 44, 140, 16))
        self.label13.setFont(font)
        self.label13.setStyleSheet(u"background-color:transparent;\n"
"")
        self.attach_btn13 = QPushButton(self.groupBox2)
        self.attach_btn13.setObjectName(u"attach_btn13")
        self.attach_btn13.setGeometry(QRect(210, 40, 100, 24))
        self.attach_btn13.setFont(font1)
        self.attach_btn13.setStyleSheet(u"QPushButton{background-color:rgba(57,167,23,220);color:white;border:0px;}\n"
"QPushButton:hover{background-color:rgba(57,167,23,255);color:white;}\n"
"QPushButton:pressed{background-color:rgba(57,167,23,235);}")
        self.label14 = QLabel(self.groupBox2)
        self.label14.setObjectName(u"label14")
        self.label14.setGeometry(QRect(20, 74, 140, 16))
        self.label14.setFont(font)
        self.label14.setStyleSheet(u"background-color:transparent;\n"
"")
        self.attach_btn14 = QPushButton(self.groupBox2)
        self.attach_btn14.setObjectName(u"attach_btn14")
        self.attach_btn14.setGeometry(QRect(210, 70, 100, 24))
        self.attach_btn14.setFont(font1)
        self.attach_btn14.setStyleSheet(u"QPushButton{background-color:rgba(57,167,23,220);color:white;border:0px;}\n"
"QPushButton:hover{background-color:rgba(57,167,23,255);color:white;}\n"
"QPushButton:pressed{background-color:rgba(57,167,23,235);}")
        self.label15 = QLabel(self.groupBox2)
        self.label15.setObjectName(u"label15")
        self.label15.setGeometry(QRect(20, 104, 161, 16))
        self.label15.setFont(font)
        self.label15.setStyleSheet(u"background-color:transparent;\n"
"")
        self.attach_btn15 = QPushButton(self.groupBox2)
        self.attach_btn15.setObjectName(u"attach_btn15")
        self.attach_btn15.setGeometry(QRect(210, 100, 100, 24))
        self.attach_btn15.setFont(font1)
        self.attach_btn15.setStyleSheet(u"QPushButton{background-color:rgba(57,167,23,220);color:white;border:0px;}\n"
"QPushButton:hover{background-color:rgba(57,167,23,255);color:white;}\n"
"QPushButton:pressed{background-color:rgba(57,167,23,235);}")
        self.label16 = QLabel(self.groupBox2)
        self.label16.setObjectName(u"label16")
        self.label16.setGeometry(QRect(20, 134, 171, 16))
        self.label16.setFont(font)
        self.label16.setStyleSheet(u"background-color:transparent;\n"
"")
        self.attach_btn16 = QPushButton(self.groupBox2)
        self.attach_btn16.setObjectName(u"attach_btn16")
        self.attach_btn16.setGeometry(QRect(210, 130, 100, 24))
        self.attach_btn16.setFont(font1)
        self.attach_btn16.setStyleSheet(u"QPushButton{background-color:rgba(57,167,23,220);color:white;border:0px;}\n"
"QPushButton:hover{background-color:rgba(57,167,23,255);color:white;}\n"
"QPushButton:pressed{background-color:rgba(57,167,23,235);}")
        self.label17 = QLabel(self.groupBox2)
        self.label17.setObjectName(u"label17")
        self.label17.setGeometry(QRect(20, 164, 181, 16))
        self.label17.setFont(font)
        self.label17.setStyleSheet(u"background-color:transparent;\n"
"")
        self.attach_btn17 = QPushButton(self.groupBox2)
        self.attach_btn17.setObjectName(u"attach_btn17")
        self.attach_btn17.setGeometry(QRect(210, 160, 100, 24))
        self.attach_btn17.setFont(font1)
        self.attach_btn17.setStyleSheet(u"QPushButton{background-color:rgba(57,167,23,220);color:white;border:0px;}\n"
"QPushButton:hover{background-color:rgba(57,167,23,255);color:white;}\n"
"QPushButton:pressed{background-color:rgba(57,167,23,235);}")
        self.label18 = QLabel(self.groupBox2)
        self.label18.setObjectName(u"label18")
        self.label18.setGeometry(QRect(20, 194, 140, 16))
        self.label18.setFont(font)
        self.label18.setStyleSheet(u"background-color:transparent;\n"
"")
        self.attach_btn18 = QPushButton(self.groupBox2)
        self.attach_btn18.setObjectName(u"attach_btn18")
        self.attach_btn18.setGeometry(QRect(210, 190, 100, 24))
        self.attach_btn18.setFont(font1)
        self.attach_btn18.setStyleSheet(u"QPushButton{background-color:rgba(57,167,23,220);color:white;border:0px;}\n"
"QPushButton:hover{background-color:rgba(57,167,23,255);color:white;}\n"
"QPushButton:pressed{background-color:rgba(57,167,23,235);}")
        self.label19 = QLabel(self.groupBox2)
        self.label19.setObjectName(u"label19")
        self.label19.setGeometry(QRect(20, 224, 161, 16))
        self.label19.setFont(font)
        self.label19.setStyleSheet(u"background-color:transparent;\n"
"")
        self.attach_btn23 = QPushButton(self.groupBox2)
        self.attach_btn23.setObjectName(u"attach_btn23")
        self.attach_btn23.setGeometry(QRect(210, 340, 100, 24))
        self.attach_btn23.setFont(font1)
        self.attach_btn23.setStyleSheet(u"QPushButton{background-color:rgba(57,167,23,220);color:white;border:0px;}\n"
"QPushButton:hover{background-color:rgba(57,167,23,255);color:white;}\n"
"QPushButton:pressed{background-color:rgba(57,167,23,235);}")
        self.label21 = QLabel(self.groupBox2)
        self.label21.setObjectName(u"label21")
        self.label21.setGeometry(QRect(20, 284, 140, 16))
        self.label21.setFont(font)
        self.label21.setStyleSheet(u"background-color:transparent;\n"
"")
        self.label20 = QLabel(self.groupBox2)
        self.label20.setObjectName(u"label20")
        self.label20.setGeometry(QRect(20, 254, 171, 16))
        self.label20.setFont(font)
        self.label20.setStyleSheet(u"background-color:transparent;\n"
"")
        self.label23 = QLabel(self.groupBox2)
        self.label23.setObjectName(u"label23")
        self.label23.setGeometry(QRect(20, 344, 161, 16))
        self.label23.setFont(font)
        self.label23.setStyleSheet(u"background-color:transparent;\n"
"")
        self.attach_btn22 = QPushButton(self.groupBox2)
        self.attach_btn22.setObjectName(u"attach_btn22")
        self.attach_btn22.setGeometry(QRect(210, 310, 100, 24))
        self.attach_btn22.setFont(font1)
        self.attach_btn22.setStyleSheet(u"QPushButton{background-color:rgba(57,167,23,220);color:white;border:0px;}\n"
"QPushButton:hover{background-color:rgba(57,167,23,255);color:white;}\n"
"QPushButton:pressed{background-color:rgba(57,167,23,235);}")
        self.label22 = QLabel(self.groupBox2)
        self.label22.setObjectName(u"label22")
        self.label22.setGeometry(QRect(20, 314, 181, 16))
        self.label22.setFont(font)
        self.label22.setStyleSheet(u"background-color:transparent;\n"
"")
        self.attach_btn21 = QPushButton(self.groupBox2)
        self.attach_btn21.setObjectName(u"attach_btn21")
        self.attach_btn21.setGeometry(QRect(210, 280, 100, 24))
        self.attach_btn21.setFont(font1)
        self.attach_btn21.setStyleSheet(u"QPushButton{background-color:rgba(57,167,23,220);color:white;border:0px;}\n"
"QPushButton:hover{background-color:rgba(57,167,23,255);color:white;}\n"
"QPushButton:pressed{background-color:rgba(57,167,23,235);}")
        self.attach_btn19 = QPushButton(self.groupBox2)
        self.attach_btn19.setObjectName(u"attach_btn19")
        self.attach_btn19.setGeometry(QRect(210, 220, 100, 24))
        self.attach_btn19.setFont(font1)
        self.attach_btn19.setStyleSheet(u"QPushButton{background-color:rgba(57,167,23,220);color:white;border:0px;}\n"
"QPushButton:hover{background-color:rgba(57,167,23,255);color:white;}\n"
"QPushButton:pressed{background-color:rgba(57,167,23,235);}")
        self.attach_btn20 = QPushButton(self.groupBox2)
        self.attach_btn20.setObjectName(u"attach_btn20")
        self.attach_btn20.setGeometry(QRect(210, 250, 100, 24))
        self.attach_btn20.setFont(font1)
        self.attach_btn20.setStyleSheet(u"QPushButton{background-color:rgba(57,167,23,220);color:white;border:0px;}\n"
"QPushButton:hover{background-color:rgba(57,167,23,255);color:white;}\n"
"QPushButton:pressed{background-color:rgba(57,167,23,235);}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Mail Sender", None))
        self.back.setText("")
        self.groupBox1.setTitle(QCoreApplication.translate("MainWindow", u"Website URLs", None))
        self.label1.setText(QCoreApplication.translate("MainWindow", u"https://icodrops.com/", None))
        self.attach_btn1.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.label2.setText(QCoreApplication.translate("MainWindow", u"https://icomarks.com/icos", None))
        self.attach_btn2.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.label3.setText(QCoreApplication.translate("MainWindow", u"https://coincodex.com/sto-list", None))
        self.attach_btn3.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.label4.setText(QCoreApplication.translate("MainWindow", u"https://cryptorank.io/", None))
        self.attach_btn4.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.label5.setText(QCoreApplication.translate("MainWindow", u"https://www.tradingview.com", None))
        self.attach_btn5.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.label6.setText(QCoreApplication.translate("MainWindow", u"https://bravenewcoin.com/", None))
        self.attach_btn6.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.label7.setText(QCoreApplication.translate("MainWindow", u"https://tradingeconomics.com", None))
        self.attach_btn12.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.label12.setText(QCoreApplication.translate("MainWindow", u"https://airdropalert.com/", None))
        self.attach_btn11.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.label9.setText(QCoreApplication.translate("MainWindow", u"https://airdropalert.com/", None))
        self.label8.setText(QCoreApplication.translate("MainWindow", u"https://data.worldbank.org/", None))
        self.label11.setText(QCoreApplication.translate("MainWindow", u"https://cryptoticker.io/en/", None))
        self.attach_btn10.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.label10.setText(QCoreApplication.translate("MainWindow", u"https://coinmarketcap.com/", None))
        self.attach_btn9.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.attach_btn7.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.attach_btn8.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.iconLabel.setText("")
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"  Scraping Tool  1.0.0", None))
        self.btnMinimize.setText("")
        self.btnClose.setText("")
        self.groupBox2.setTitle(QCoreApplication.translate("MainWindow", u"Website URLs", None))
        self.label13.setText(QCoreApplication.translate("MainWindow", u"https://airdrops.io/", None))
        self.attach_btn13.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.label14.setText(QCoreApplication.translate("MainWindow", u"https://coincodex.com/", None))
        self.attach_btn14.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.label15.setText(QCoreApplication.translate("MainWindow", u"https://cryptorank.io/price/", None))
        self.attach_btn15.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.label16.setText(QCoreApplication.translate("MainWindow", u"https://www.coingecko.com/", None))
        self.attach_btn16.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.label17.setText(QCoreApplication.translate("MainWindow", u"https://www.livecoinwatch.com", None))
        self.attach_btn17.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.label18.setText(QCoreApplication.translate("MainWindow", u"https://coinranking.com/", None))
        self.attach_btn18.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.label19.setText(QCoreApplication.translate("MainWindow", u"https://airdrops.io/airdrop/", None))
        self.attach_btn23.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.label21.setText(QCoreApplication.translate("MainWindow", u"https://airdropalert.com/", None))
        self.label20.setText(QCoreApplication.translate("MainWindow", u"https://www.airdropbob.com", None))
        self.label23.setText(QCoreApplication.translate("MainWindow", u"https://coinmarketcap.com/", None))
        self.attach_btn22.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.label22.setText(QCoreApplication.translate("MainWindow", u"https://www.airdropsmob.com", None))
        self.attach_btn21.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.attach_btn19.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.attach_btn20.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
    # retranslateUi

