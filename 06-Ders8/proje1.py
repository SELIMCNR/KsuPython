import sys
from PyQt6.QtWidgets import *
from form1 import *


class AnaForm(Ui_MainWindow,QMainWindow):
    def __init__(self) :
        super(AnaForm,self).__init__()
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.EKLE)
        self.listWidget.itemClicked.connect(self.Tıkla)
        self.pushButton_2.clicked.connect(self.Sil)
        self.listWidget.doubleClicked(self.Sil)
        self.pushButton_3.connect(self.INSERT)

    def Insert(self):
        self.listWidget.insertItem(
            self.satirNo, self.lineEdit())  # araya eleman ekleme

    def Sil(self):
        secilieleman = self.listWidget.takeItem(self.satirNo)
        self.listWidget.removeItemWidget(secilieleman)

    def EKLE(self):
        meyveler = ["e", "a", "k", "k", "k"]
        self.listWidget.addItems(meyveler)

    def Tıkla(self):
        x = self.listWidget.currentItem().text()
        self.satirNo = self.listWidget.currentRow()
        self.label.setText(str(self.satirNo)+"-"+x)


proje1 = QApplication(sys.argv)
form1 = AnaForm()
form1.show()
sys.exit(proje1.exec())
