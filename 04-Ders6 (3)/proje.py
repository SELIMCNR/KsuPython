
import sys
from PyQt5.QtWidgets import *
from form1 import Ui_MainWindow
class AnaForm(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super(AnaForm,self).__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.Ekle)         #buttona tıklayınca Ekle fonksiyonu çalıştır
      ## self.pushButton_2.clicked.connect(self.Arayaekle)
        self.listWidget.itemClicked.connect(self.EtiketeYaz) #EtiketeYaz fonksiyonuna liste içerisinde elemanı yazdır
        self.pushButton_2.clicked.connect(self.Temizle)  #buttona tıklayınca Temizle fonksiyonu çalıştır
        self.pushButton_3.clicked.connect(self.ArayaEkle) 
        self.listWidget.doubleClicked.connect(self.Sil)
        
    def Sil(self):
          pass  
          # self.listWidget.deleteLater()
     
     
    def Temizle(self):
            self.listWidget.clear()   #List widget içerisini temizle
           # MyList=["No1","No2","No3","No4"]            
           # self.listWidget.addItems(MyList)  #Listwidget içerisine listeyi ekle
              
     
        
    def EtiketeYaz(self):
            x=self.listWidget.currentItem().text()   #x değişkeni içerisine listWidget'daki elemanları yazdır
            self.label.setText(x)                    # label içerisine liste içindeki tıklanan elemanı yaz
            a=self.listWidget.currentRow()           # liste içerisinde elemanın satır numarasını görüntüle
            print(a)
        
        
    def Ekle(self):
        x=self.lineEdit.text()                      #x değişkenine lineEdit'ten gelen değerleri ekle
        self.listWidget.addItem(x)                  #listWidget'a  x değişkeninin değerlerini ekle
        self.lineEdit.setText(None)          
        
        
    def ArayaEkle(self):
        x=self.lineEdit.text()
        index=self.listWidget.currentRow()
        self.listWidget.insertItem(index,x) 
        
        
proje1=QApplication(sys.argv)
form1=AnaForm()
form1.show()
proje1.exec()     
            