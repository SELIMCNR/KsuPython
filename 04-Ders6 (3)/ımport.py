import sys
from PyQt5.QtWidgets import *
from form1 import Ui_MainWindow
class AnaForm(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super(AnaForm,self).__init__()
        self.setupUi(self)
proje1=QApplication(sys.argv)
form1=AnaForm()
form1.show()
proje1.exec()   