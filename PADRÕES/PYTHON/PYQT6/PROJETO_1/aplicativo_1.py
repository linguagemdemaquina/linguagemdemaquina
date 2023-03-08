import sys

import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# Sub-Classe que define padrões da tela principal
class home(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplicativo 1 Teste - Python")
        self.setStyleSheet('background-color: #666666')
        self.resize(300,600)
  

aplicativo = QApplication(sys.argv)

janelaInicial = home()
janelaInicial.show()

aplicativo.exec()