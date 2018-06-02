# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created: Fri Feb 23 12:56:23 2018
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.plus = QtGui.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(240, 230, 51, 31))
        self.plus.setObjectName(_fromUtf8("plus"))
        self.first_input = QtGui.QLineEdit(self.centralwidget)
        self.first_input.setGeometry(QtCore.QRect(240, 140, 61, 41))
        self.first_input.setObjectName(_fromUtf8("first_input"))
        self.second_input = QtGui.QLineEdit(self.centralwidget)
        self.second_input.setGeometry(QtCore.QRect(430, 140, 61, 41))
        self.second_input.setObjectName(_fromUtf8("second_input"))
        self.minus = QtGui.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(310, 232, 51, 31))
        self.minus.setObjectName(_fromUtf8("minus"))
        self.mutli = QtGui.QPushButton(self.centralwidget)
        self.mutli.setGeometry(QtCore.QRect(380, 232, 51, 31))
        self.mutli.setObjectName(_fromUtf8("mutli"))
        self.output = QtGui.QLabel(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(330, 320, 121, 31))
        self.output.setText(_fromUtf8(""))
        self.output.setObjectName(_fromUtf8("output"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 320, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.div = QtGui.QPushButton(self.centralwidget)
        self.div.setGeometry(QtCore.QRect(450, 232, 51, 31))
        self.div.setObjectName(_fromUtf8("div"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
#my code
        self.plus.clicked.connect(self.p)
        self.minus.clicked.connect(self.m)
        self.mutli.clicked.connect(self.mt)
        self.div.clicked.connect(self.d)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #my function
    def p(self):
        a = self.first_input.text()
        b = self.second_input.text()
        sum = float(a) + float(b)
        sum=  str(sum)
        self.output.setText(sum)
        
    def m(self):
        a = self.first_input.text()
        b = self.second_input.text()
        sum = float(a) - float(b)
        sum=  str(sum)
        self.output.setText(sum)
        
    def mt(self):
        a = self.first_input.text()
        b = self.second_input.text()
        sum = float(a) * float(b)
        sum=  str(sum)
        self.output.setText(sum)
        
    def d(self):
        a = self.first_input.text()
        b = self.second_input.text()
        
        if float(b)==0:
            sum="Cannot divide by zero"            
        else:
            sum = float(a)/ float(b)
            sum=  str(sum)
        self.output.setText(sum)
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.plus.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.minus.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.mutli.setText(QtGui.QApplication.translate("MainWindow", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Answer:", None, QtGui.QApplication.UnicodeUTF8))
        self.div.setText(QtGui.QApplication.translate("MainWindow", "/", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

