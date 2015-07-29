#-*- coding: gb2312 -*-

import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets

class MainWindow( QtWidgets.QMainWindow ):
    def __init__(self):
        super( QtWidgets.QMainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(800,600)
        self.center()
        self.setWindowTitle('Hercales Layout')
        self.setWindowIcon(QtGui.QIcon\
        ('icons/icon.ico'))

        menu_control = self.menuBar().addMenu('Contorl')
        act_quit = menu_control.addAction('Exit')
        act_quit.triggered.connect(self.close)

        menu_help = self.menuBar().addMenu('Help')
        act_help = menu_help.addAction('Help (F1)')
        act_help.triggered.connect(self.help)
        act_about = menu_help.addAction('About...')
        act_about.triggered.connect(self.about)
        act_aboutqt = menu_help.addAction('About Qt')
        act_aboutqt.triggered.connect(self.aboutqt)

        self.statusBar().showMessage('Ready')
        self.show()

    def about(self):
        QtWidgets.QMessageBox.about(self,"About","Hercales Layout v0.1 alpha \nNave, Niu")

    def help(self):
        QtWidgets.QMessageBox.about(self,"Help","Documents : \nHttp://neverland.pw/hercales/ ")

    def aboutqt(self):
        QtWidgets.QMessageBox.aboutQt(self)

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question\
        (self, 'Info',
            "Are you sure to exit Hercales?",
             QtWidgets.QMessageBox.Yes,
             QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2,\
         (screen.height()-size.height())/2)

myapp =QtWidgets.QApplication(sys.argv)
mainwindow = MainWindow()
sys.exit(myapp.exec_())