import sys 
from PyQt5.QtWidgets import *
from form1 import Ui_MainWindow

class AnaFrom(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super(AnaFrom,self).__init__()
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.Ekle)                               
        self.pushButton_3.clicked.connect(self.Doldur)
        self.pushButton_4.clicked.connect(self.Temizle)
        self.tableWidget.doubleClicked.connect(self.Sec)
    
    
    def Sec(self):
        secim=self.tableWidget.selectedItems() #tablo hücresindeki bir değeri liste yapar
        self.label.setText(secim[0].text()) #secilen elamanı labela yazar
    
        
    def Temizle(self):
          self.tableWidget.clear()    
              
    def Doldur(self):
        self.tableWidget.setHorizontalHeaderLabels(('Öğr no','öğrenci ad','öğrenci soyad')) #başlık değiştirir
        ogrenci=[["12","Name","Surname"],["15","Name1","Surname2"],["15","Name1","Surname2"]
                 ,["15","Name1","Surname2"],["15","Name1","Surname2"]]
    #    self.tableWidget.setItem(0,0,QTableWidgetItem(ogrenci[0]))
    #   self.tableWidget.setItem(0,0,QTableWidgetItem(ogrenci[1]))
    #    self.tableWidget.setItem(0,0,QTableWidgetItem(ogrenci[2]))
        
        i=0
        for x in ogrenci : 
            j=0 
            self.tableWidget.insertRow(x) #table nesnesine ilk satırı ekledi
            for y in ogrenci:
                 self.tableWidget.setItem(i,j,QTableWidgetItem(ogrenci[y]))
                 j=j+1
            i+=1     
        
    def Ekle(self):
        self.tableWidget.insertRow(0)
        self.tableWidget.setItem(1,1,QTableWidgetItem())
        
  
            
proje1=QApplication(sys.argv)
form1=AnaFrom()
sys.exit(proje1.exec()) 

#Ödev seçilen elemandan yeni liste oluşturacak list widget yap.