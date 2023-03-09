import sys

from PyQt6.QtCore import Qt 
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QVBoxLayout, QMainWindow

aplicativo = QApplication(sys.argv)

class janelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        #Define as características da janela principal
        self.setWindowTitle('Aplicativo 1 - Python PyQt6')
        self.resize(300,600)
        self.setStyleSheet('background-color: #666666; color:#FFFFFF;')
        
        
        #Define o título da seção e suas características
        titulo = QLabel(self)
        titulo.setText('Programando com Python - PyQT6')
        titulo.setStyleSheet('margin-top:5px; font-size:14px; font-weight:bold;')
        titulo.show()

        self.setCentralWidget(titulo)
        titulo.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        


home = janelaPrincipal()
home.show()

aplicativo.exec()