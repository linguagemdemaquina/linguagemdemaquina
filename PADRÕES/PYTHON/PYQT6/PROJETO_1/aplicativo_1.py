import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel

aplicativo = QApplication(sys.argv)

home = QWidget()
home.resize(300,600)
home.setWindowTitle("Aplicativo 1 - Python")
home.setStyleSheet('background-color: #666666')
home.show()



aplicativo.exec()