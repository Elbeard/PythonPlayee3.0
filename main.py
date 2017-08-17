# -*- coding: utf-8 -*-
import sys
import os
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QMainWindow, QApplication, QStatusBar)
from PyQt5.QtGui import QIcon


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #--------------------------- Кнопки -------------------------------#
        playButton = QPushButton("Play", self)
        playButton.move(10, 10)

        stopButton = QPushButton("Stop", self)
        stopButton.move(110, 10)

        openButton = QPushButton("Open", self)
        openButton.move(210, 10)


        playButton.clicked.connect(mainWindow.buttonClicked)
        stopButton.clicked.connect(mainWindow.buttonClicked)
        openButton.clicked.connect(mainWindow.buttonClicked)

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

    def buttonClicked(self):
        sender = self.sender()
        self.view.statusBar().showMessage(sender.text() + ' was pressed')

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        f = open(fname, 'r')
        with f:
            data = f.read()
            self.textEdit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Controller()
    sys.exit(app.exec_())