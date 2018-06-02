# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'downloader.ui'
#
# Created: Fri Feb 23 15:53:53 2018
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
        self.url = QtGui.QLineEdit(self.centralwidget)
        self.url.setGeometry(QtCore.QRect(170, 150, 501, 41))
        self.url.setObjectName(_fromUtf8("url"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 150, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.d_button = QtGui.QPushButton(self.centralwidget)
        self.d_button.setGeometry(QtCore.QRect(320, 270, 181, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(12)
        self.d_button.setFont(font)
        self.d_button.setObjectName(_fromUtf8("d_button"))
        self.output = QtGui.QLabel(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(320, 360, 151, 51))
        self.output.setText(_fromUtf8(""))
        self.output.setObjectName(_fromUtf8("output"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
    #my code
        self.d_button.clicked.connect(self.startDownload)

        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
#my function
    def startDownload(self):
        url1=self.url.text()
        url1=str(url1)

        try:
            
            import urllib2
            response = urllib2.urlopen(url1) #variable t check the servers reponce
        #urlopen() wil open the url
            with open("fielname.pdf", "wb") as f: #wb = write mode
                f.write(response.read())
                f.close()
            self.output.setText("Error!")
            
        except:
            self.output.setText("Error!")

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Enter URL:", None, QtGui.QApplication.UnicodeUTF8))
        self.d_button.setText(QtGui.QApplication.translate("MainWindow", "Download it!", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

