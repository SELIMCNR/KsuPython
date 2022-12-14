# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Yenipencere(object):
    def setupUi(self, Yenipencere):
        Yenipencere.setObjectName("Yenipencere")
        Yenipencere.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Yenipencere)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 90, 47, 13))
        self.label.setObjectName("label")
        Yenipencere.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Yenipencere)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Yenipencere.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Yenipencere)
        self.statusbar.setObjectName("statusbar")
        Yenipencere.setStatusBar(self.statusbar)

        self.retranslateUi(Yenipencere)
        QtCore.QMetaObject.connectSlotsByName(Yenipencere)

    def retranslateUi(self, Yenipencere):
        _translate = QtCore.QCoreApplication.translate
        Yenipencere.setWindowTitle(_translate("Yenipencere", "MainWindow"))
        self.pushButton.setText(_translate("Yenipencere", "Kapat"))
        self.label.setText(_translate("Yenipencere", "TextLabel"))

