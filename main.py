# -*- coding: utf-8 -*-
import sys
import os
from PyQt5.QtWidgets import (QWidget, QPushButton, QFileDialog,
                             QMainWindow, QApplication, QStatusBar)
from PyQt5.QtGui import QIcon


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.controller = Controller()
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

        self.playButton.clicked.connect(self.controller.buttonClicked)
        self.stopButton.clicked.connect(self.controller.buttonClicked)
        self.openButton.clicked.connect(self.controller.openFile)

        #----------------------- Параметры главного окна ----------------------#
        self.setGeometry(80, 140, 400, 150)
        self.setWindowTitle('Питониум')
        self.scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QIcon(self.scriptDir + os.path.sep + 'butterfly green.ico'))
        self.show()


class Controller(QWidget):

    def buttonClicked(self):
        sender = self.sender()
        mainWindow.statusBar().showMessage(sender.text() + ' was pressed')

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        mainWindow.statusBar().showMessage('File is opened')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = View()
    sys.exit(app.exec_())