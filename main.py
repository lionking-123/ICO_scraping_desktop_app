from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from functools import partial
from icodrops import icodrops
# from analytics import  AnalyticsWidget

import os
import sys
import time
from multiprocessing import Process

# ============= Const variables define part =============

FROM_RESET, _ = loadUiType(os.path.join(
    os.path.dirname(__file__), "./UI/reset.ui"))

# ============= Worker Class for Worker Thread ============


class Worker(QObject):
    finished = pyqtSignal()
    scrap_id = 0

    def run(self):
        if(self.scrap_id == 1):
            icodrops()

        self.finished.emit()

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
        self.attach_btn1.clicked.connect(self.scrape_icodrops)

    def scrape_icodrops(self):
        self.thread = QThread()
        self.worker = Worker()
        self.worker.scrap_id = 1
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # Step 6: Start the thread
        self.thread.start()
        self.attach_btn1.setEnabled(False)
        self.attach_btn2.setEnabled(False)
        self.attach_btn3.setEnabled(False)
        self.attach_btn4.setEnabled(False)
        self.attach_btn5.setEnabled(False)
        self.attach_btn6.setEnabled(False)
        self.attach_btn7.setEnabled(False)
        self.attach_btn8.setEnabled(False)
        self.attach_btn9.setEnabled(False)
        self.attach_btn10.setEnabled(False)
        self.attach_btn11.setEnabled(False)
        self.attach_btn12.setEnabled(False)
        self.attach_btn13.setEnabled(False)
        self.attach_btn14.setEnabled(False)
        self.attach_btn15.setEnabled(False)
        self.attach_btn16.setEnabled(False)
        self.attach_btn17.setEnabled(False)
        self.attach_btn18.setEnabled(False)
        self.attach_btn19.setEnabled(False)
        self.attach_btn20.setEnabled(False)
        self.attach_btn21.setEnabled(False)
        self.attach_btn22.setEnabled(False)
        self.attach_btn23.setEnabled(False)
        self.attach_btn1.setText("Extracting ...")

        self.thread.finished.connect(
            lambda: (self.attach_btn1.setEnabled(True),
                     self.attach_btn2.setEnabled(True),
                     self.attach_btn3.setEnabled(True),
                     self.attach_btn4.setEnabled(True),
                     self.attach_btn5.setEnabled(True),
                     self.attach_btn6.setEnabled(True),
                     self.attach_btn7.setEnabled(True),
                     self.attach_btn8.setEnabled(True),
                     self.attach_btn9.setEnabled(True),
                     self.attach_btn10.setEnabled(True),
                     self.attach_btn11.setEnabled(True),
                     self.attach_btn12.setEnabled(True),
                     self.attach_btn13.setEnabled(True),
                     self.attach_btn14.setEnabled(True),
                     self.attach_btn15.setEnabled(True),
                     self.attach_btn16.setEnabled(True),
                     self.attach_btn17.setEnabled(True),
                     self.attach_btn18.setEnabled(True),
                     self.attach_btn19.setEnabled(True),
                     self.attach_btn20.setEnabled(True),
                     self.attach_btn21.setEnabled(True),
                     self.attach_btn22.setEnabled(True),
                     self.attach_btn23.setEnabled(True),
                     self.attach_btn1.setText("Extract"))
        )

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
