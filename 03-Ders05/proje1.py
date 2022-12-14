import sys
from typing_extensions import Self
from PyQt6.QtWidgets import *
from form2 import Ui_MainWindow


class Anaform(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(Anaform, self).__init__()
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.comboEkle)
        self.comboBox.activated.connect(self.textEditEkle)
        
    def comboEkle(self):
        x=self.lineEdit.text()  #dışardan veri gir 
        self.comboBox.addItem(x)  # comboboxa ekle
    
    def textEditEkle(self):
        x= self.comboBox.currentText()
        self.textEdit.append(x)
        
proje1 = QApplication(sys.argv)
form2 = Anaform()
sys.exit(proje1.exec())




