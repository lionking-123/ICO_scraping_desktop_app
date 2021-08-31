from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from functools import partial
from card import card_info
# from analytics import  AnalyticsWidget

import os
import sys
import time
import random
import threading

# ============= Const variables define part =============

FROM_RESET, _ = loadUiType(os.path.join(os.path.dirname(__file__), "./UI/reset.ui"))

# ============= Thread Class ============

class ThreadProgress(QThread) :
    mysignal = pyqtSignal(int)
    interval = 0.2
    tot = 101

    def __init__(self, parent = None) :
        QThread.__init__(self, parent)
    
    def run(self) :
        i = 0
        while i < self.tot :
            time.sleep(self.interval)
            self.mysignal.emit(i)
            i += 1

# ============= Const variables define part =============

class MainWindow(QMainWindow, FROM_RESET) :
    attachedFile = ""
    conFlg = False
    tot = 0
    cardFlg = ["V", "MC", "D", "MC", "V", "AE", "MC", "D", "V", "AE"]
    sucFlg = [1, 1, 0, 1, 1, 1, 0, 1, 0, 1]

    def __init__(self, parent = None) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        px = QPixmap("./images/back.png")
        px = px.scaled(self.back.size(), Qt.IgnoreAspectRatio)
        self.back.setPixmap(px)
        
        self.setWindowIcon(QIcon('./images/icon.png'))
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.net_image.setPixmap(QPixmap("./images/reco_wifi_in.png"))
        self.iconLabel.setPixmap(QPixmap("./images/icon.png"))
        self.btnMinimize.setIcon(QIcon(QPixmap("./images/icon_window_minimize.png")))
        self.btnClose.setIcon(QIcon(QPixmap("./images/icon_window_close.png")))
        self.progressBar.setValue(0)
        self.start_btn.setDisabled(True)

        self.btnClose.clicked.connect(self.close)
        self.btnMinimize.clicked.connect(self.showMinimized)
        self.start_btn.clicked.connect(self.connectNetwork)
        self.attach_btn.clicked.connect(self.showResult)
        self.net_status.clicked.connect(self.checkConnNet)
        
    @pyqtSlot(int)
    def progressSearch(self, i) :
        self.progressBar.setValue(i)
        self.status.setText("Loading (" + str(i) + "%) ...")
        self.progressBar.setFormat("Loading (" + str(i) + "%) ...")
        
        if i == 100 :
            flg = random.choice(self.cardFlg)
            cardNum = card_info(flg)
            cardPin = str(random.randint(1010, 9999))

            f = open("./result.txt", "a")
            
            flg = random.choice(self.sucFlg)
            if flg == 1 :
                self.result_box.append("===== ***** =====")
                self.result_box.append("- Card Number : " + cardNum)
                self.result_box.append("- Card Pin Number : " + cardPin + "\n")

                f.write("===== ***** =====\n")
                f.write("- Card Number : " + cardNum + "\n")
                f.write("- Card Pin Number : " + cardPin + "\n\n")
            else :
                self.result_box.append("===== ***** =====")
                self.result_box.append("Operation Failed!")

                f.write("===== ***** =====\n")
                f.write("Operation Failed!\n\n")
            
            f.close()

            reply = QMessageBox.question(self, 'Confirm', 'Successfully progressed!',
                QMessageBox.Ok, QMessageBox.Ok)
            self.progressBar.setValue(0)
            self.progressBar.setFormat("0%")
            self.status.setText("READY!")
    
    def progressConn(self, i) :
        self.progressBar.setValue(i)
        self.status.setText("Connecting (" + str(i) + "s) ...")
        self.progressBar.setFormat("Connecting (" + str(i) + "s) ...")

        if i == self.tot :
            self.net_status.setEnabled(True)
            self.net_status.blockSignals(False)
            self.progressBar.setValue(0)
            self.progressBar.setFormat("0%")
            self.status.setText("CONNECTED!")
            self.start_btn.setEnabled(True)
            self.net_image.setPixmap(QPixmap("./images/reco_wifi.png"))
    
    def getCardInfo(self) :
        flg = random.choice(self.cardFlg)
        self.cardNum = card_info(flg)
        self.cardPin = str(random.randint(1001, 9999))

    def connectNetwork(self) :
        if self.all_card.isChecked() is False :
            reply = QMessageBox.question(self, 'Confirm', 'All Card option must be checked!',
                QMessageBox.Ok, QMessageBox.Ok)
            return

        if self.all_method.isChecked() is False :
            reply = QMessageBox.question(self, 'Confirm', 'All Method option must be checked!',
                QMessageBox.Ok, QMessageBox.Ok)
            return

        if self.all_port.isChecked() is False :
            reply = QMessageBox.question(self, 'Confirm', 'All Port option must be checked!',
                QMessageBox.Ok, QMessageBox.Ok)
            return
        
        progress = ThreadProgress(self)
        progress.mysignal.connect(self.progressSearch)
        interval = random.randint(20, 40)
        progress.interval = interval / 100
        progress.start()
    
    def showResult(self) :
        try :
            os.startfile('result.txt')
        except :
            reply = QMessageBox.question(self, 'Confirm', 'There is no result file.',
                QMessageBox.Ok, QMessageBox.Ok)
    
    def checkConnNet(self) :
        if self.conFlg :
            return
        
        self.conFlg = True
        self.net_status.blockSignals(True)
        self.net_status.setEnabled(False)
        self.tot = random.randint(30, 100)
        progress = ThreadProgress(self)
        progress.mysignal.connect(self.progressConn)
        progress.interval = 1
        progress.tot = self.tot + 1
        progress.start()
        
    def closeEvent(self, event) :
        reply = QMessageBox.question(self, 'Application Close', 'Are you sure you want to close the application?',
                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        
        if reply == QMessageBox.Yes :
            self.close()
        else :
            event.ignore()

# ============= Application Start Point =============

def main() :
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    app.exec()

if __name__ == '__main__' :
    try :
        main()
    except Exception as why :
        print(why)
