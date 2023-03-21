# Powered by Linguagem de Máquina using PyQT6
# ==========================================================

# Resources and documentations : 
# https://www.riverbankcomputing.com/static/Docs/PyQt6/ 
# ==========================================================

import sys
from pathlib import Path
from PyQt6.QtWidgets import QApplication,  QWidget, QLabel, QLineEdit, QPushButton,  QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('SISTEMA DE GESTÃO')
        self.setWindowIcon(QIcon('./imagens/logomarca.png'))
        self.setFixedWidth(300)
        self.setFixedHeight(600)

        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.setContentsMargins(10,0,10,220)
        layout.setObjectName('layout')
        
        imagemLogomarca = QLabel()
        logomarcaGrande = QPixmap('./imagens/logomarca_horizontal.png')
        imagemLogomarca.setPixmap(logomarcaGrande)
        imagemLogomarca.setObjectName('imagemLogomarcaHorizontal')

        tituloDeSecao = QLabel('LOGIN DE SISTEMA')
        tituloDeSecao.setObjectName('tituloDeSecao')

        
        tituloEmail = QLabel ('EMAIL')
        tituloEmail.setObjectName('tituloEmail')
        
        email = QLineEdit(self)
        email.setPlaceholderText('DIGITE SEU EMAIL')
        email.setObjectName('email')

        tituloSenha = QLabel('SENHA')
        tituloSenha.setObjectName('tituloSenha')

        senha = QLineEdit(self)
        senha.setEchoMode(QLineEdit.EchoMode.Password)
        senha.setPlaceholderText('DIGITE SUA SENHA')
        senha.setObjectName('senha')
        
        botao_login = QPushButton('LOGIN')
        botao_login.setObjectName('botaoLogin')

        layout.addWidget(imagemLogomarca)
        layout.addWidget(tituloDeSecao)        
        layout.addWidget(tituloEmail)
        layout.addWidget(email)
        layout.addWidget(tituloSenha)
        layout.addWidget(senha)
        layout.addWidget(botao_login)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    app.setStyleSheet(Path('.\\qss\estilo.qss').read_text())
    window = MainWindow()
    sys.exit(app.exec())