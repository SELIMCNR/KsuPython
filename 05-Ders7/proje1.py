import sys
from PyQt5.QtWidgets import * 
from form1 import Ui_MainWindow
from form2 import Ui_Yenipencere 
    
class AnaForm(QMainWindow,Ui_MainWindow):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.GOSTER)
    def GOSTER(self):
        self.Form2 = ikinciForm()
        self.Form2.label.setText("GEÇTİK")
class ikinciForm(QMainWindow,Ui_Yenipencere):
        def __init__(self) :
            super().__init__()
            self.setupUi(self)
            self.show()
            self.pushButton.clicked.connect(self.KAPAT)
        def KAPAT (self):
            pass
        
        
proje1 = QApplication(sys.argv)
form1 = AnaForm()
proje1.exec_() 