
import sys
from PyQt6.QtWidgets import *
from form2 import Ui_MainWindow


class AnaForm(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(AnaForm, self).__init__()
        self.setupUi(self)
        self.show()
        self.radioButton.clicked.connect(lambda: self.EtiketeYaz(
            self.radioButton))  # lamda: özel bir fonksiyon
        self.radioButton_2.clicked.connect(
            lambda: self.EtiketeYaz(self.radioButton_2))
        self.radioButton_3.clicked.connect(
            lambda: self.EtiketeYaz(self.radioButton_3))

    # a parametresi lambda dan gelen radioButton ların 3'ünü içeriyor.
    def EtiketeYaz(self, a):
        x = a.text()
        self.label.setText(x)


proje2 = QApplication(sys.argv)
form2 = AnaForm()
form2.show()
sys.exit(proje2.exec())
