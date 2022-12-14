import sys
from PyQt6.QtWidgets import *
from form2 import Ui_MainWindow


class AnaForm(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(AnaForm, self).__init__()
        self.setupUi(self)


proje2 = QApplication(sys.argv)
form1 = AnaForm()
form1.show()
sys.exit(proje2.exec())
