import sys
from turtle import pencolor
from PyQt6.QtWidgets import *


class MyWin():
    def __call__(self):
        super(self).__init__()
        self.formuKur(self)
        

    def formuKur(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("Merhaba Dünya")
        self.adi = QLabel(self)
        self.adi.move(84, 100)
        self.adi.setText = "Matematik"
        self.show()


proje = QApplication(sys.argv)
pencere = MyWin()
sys.exit(proje.exec())
