# Powered by Linguagem de Máquina using PyQT6
# ==========================================================

# Resources and documentations : 
# https://www.riverbankcomputing.com/static/Docs/PyQt6/ 
# ==========================================================

import sys
import os

from pathlib import Path

caminho_relativo = os.getcwd()
caminho_relativo = caminho_relativo + '\PADRÕES\PYTHON\PYQT6\PROJETO_1'
caminho_logomarca = caminho_relativo + '\imagens\logomarca.png'
caminho_logomarca_horizontal = caminho_relativo + '\imagens\logomarca_horizontal.png' 
caminho_imagem_instagram = caminho_relativo + '\imagens\instagram.png'

caminho_qss = caminho_relativo +  '\qss\estilo.qss'

from PyQt6.QtWidgets import QApplication,  QWidget, QLabel, QLineEdit, QPushButton,  QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap, QCursor


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('SISTEMA DE GESTÃO INTEGRADA')
        self.setWindowIcon(QIcon(caminho_logomarca))
        self.setFixedWidth(300)
        self.setFixedHeight(500)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(10,10,10,10)
        layout.setObjectName('layout')
        self.setLayout(layout)
        
        imagemLogomarca = QLabel()
        logomarcaGrande = QPixmap(caminho_logomarca_horizontal)
        imagemLogomarca.setPixmap(logomarcaGrande)
        imagemLogomarca.setObjectName('imagemLogomarcaHorizontal')
        imagemLogomarca.setAlignment(Qt.AlignmentFlag.AlignCenter)


        tituloDeSecao = QLabel('ERP - SISTEMA DE GESTÃO INTEGRADA')
        tituloDeSecao.setObjectName('tituloDeSecao')
        tituloDeSecao.setAlignment(Qt.AlignmentFlag.AlignCenter)

        
        tituloEmail = QLabel ('EMAIL')
        tituloEmail.setObjectName('tituloEmail')
        tituloEmail.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        
        email = QLineEdit(self)
        email.setPlaceholderText('DIGITE SEU EMAIL')
        email.setObjectName('email')
        

        tituloSenha = QLabel('SENHA')
        tituloSenha.setObjectName('tituloSenha')
        tituloSenha.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        senha = QLineEdit(self)
        senha.setEchoMode(QLineEdit.EchoMode.Password)
        senha.setPlaceholderText('DIGITE SUA SENHA')
        senha.setObjectName('senha')
        
        botao_login = QPushButton('LOGIN')
        botao_login.setObjectName('botaoLogin')
        botao_login.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        botaoInstagram = QPushButton('INSTAGRAM')
        instagram = QIcon(QPixmap(caminho_imagem_instagram))
        botaoInstagram.setIcon(instagram)
        botaoInstagram.setObjectName('botaoInstagram')
        botaoInstagram.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

 

              
        layout.addWidget(imagemLogomarca)
        layout.addWidget(tituloDeSecao)        
        layout.addWidget(tituloEmail)
        layout.addWidget(email)
        layout.addWidget(tituloSenha)
        layout.addWidget(senha)
        layout.addWidget(botao_login, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(botaoInstagram, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    
    app.setStyleSheet(Path(caminho_qss).read_text())
    window = MainWindow()
    sys.exit(app.exec())