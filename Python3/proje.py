
import sys
from PyQt6.QtWidgets import *
from form1 import Ui_MainWindow


class AnaForm(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(AnaForm, self).__init__()
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.ekle)  # buttona tıklayınca ekleme yap combo boxa
        self.comboBox.activated.connect(self.EtiketeYaz)  #combo boxa tıklayınca ekle
        self.pushButton_2.clicked.connect(self.temizle)   #buttona tıklayınca comboboxı temizle
        self.pushButton_3.clicked.connect(self.Arayaekle)   
        self.pushButton_4.clicked.connect(self.Sil)
     
      
    def Sil(self):
         pass 
      
    def ekle(self):
           x=self.lineEdit.text()                      #x değişkenine lineEdit'ten gelen değerleri ekle
           self.comboBox.addItem(x)                  #comboBox'a  x değişkeninin değerlerini ekle
           self.lineEdit.setText(None)   

    # a parametresi lambda dan gelen radioButton ların 3'ünü içeriyor.
    def EtiketeYaz(self):
        x = self.comboBox.currentText()             #Combo boxda tıklanan değeri al 
        self.label.setText(x)                       #label öğesine ekle  
       
    def temizle(self):
        self.comboBox.clear()   # comboboxı temizle

    def Arayaekle(self):
        x=self.lineEdit.text()
        index=self.comboBox.currentIndex() #seçilen indexe ekler
        self.comboBox.insertItem(index,x)
proje = QApplication(sys.argv)
form1 = AnaForm()
form1.show()
sys.exit(proje.exec())
