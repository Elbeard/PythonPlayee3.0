# -*- coding: utf-8 -*-
import sys
import os

import self as self
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QMainWindow, QApplication, QStatusBar)
from PyQt5.QtGui import QIcon


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #--------------------------- Кнопки -------------------------------#
        self.playButton = QPushButton("Play", self)
        self.playButton.move(10, 10)

        self.stopButton = QPushButton("Stop", self)
        self.stopButton.move(110, 10)

        self.openButton = QPushButton("Open", self)
        self.openButton.move(210, 10)

        self.statusBar
        self.statusBar().showMessage("Работает")


        #----------------------- Параметры главного окна ----------------------#
        self.setGeometry(80, 140, 400, 150)
        self.setWindowTitle('Питониум')
        self.scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QIcon(self.scriptDir + os.path.sep + 'butterfly green.ico'))
        self.show()


class Controller:
    def __init__(self):
        self.view = View()

        self.view.playButton.clicked.connect()
        self.view.stopButton.clicked.connect()
        self.view.openButton.clicked.connect()

    def buttonClicked(self):
        sender = self.sender()
        self.view.statusBar().showMessage(sender.text() + ' was pressed')

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        #f = open(fname, 'r')
        #with f:
        #    data = f.read()
        #    self.textEdit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Controller()
    sys.exit(app.exec_())