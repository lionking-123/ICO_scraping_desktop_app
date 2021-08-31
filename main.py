from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from functools import partial
# from analytics import  AnalyticsWidget

import os
import sys
import time
import random

# ============= Const variables define part =============

FROM_RESET, _ = loadUiType(os.path.join(
    os.path.dirname(__file__), "./UI/reset.ui"))


# ============= Const variables define part =============

class MainWindow(QMainWindow, FROM_RESET):

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.setupUi(self)

        px = QPixmap("./images/back.png")
        px = px.scaled(self.back.size(), Qt.IgnoreAspectRatio)
        self.back.setPixmap(px)

        self.setWindowIcon(QIcon('./images/icon.png'))
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.iconLabel.setPixmap(QPixmap("./images/icon.png"))
        self.btnMinimize.setIcon(
            QIcon(QPixmap("./images/icon_window_minimize.png")))
        self.btnClose.setIcon(QIcon(QPixmap("./images/icon_window_close.png")))

        self.btnClose.clicked.connect(self.close)
        self.btnMinimize.clicked.connect(self.showMinimized)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Application Close', 'Are you sure you want to close the application?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            self.close()
        else:
            event.ignore()

# ============= Application Start Point =============


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()


if __name__ == '__main__':
    try:
        main()
    except Exception as why:
        print(why)
