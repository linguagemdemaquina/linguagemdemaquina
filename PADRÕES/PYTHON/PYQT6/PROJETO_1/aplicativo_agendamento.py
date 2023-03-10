import sys

from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QPushButton, QLineEdit, QCalendarWidget 

aplicativo = QApplication(sys.argv)

janela =  QWidget()
janela.setWindowTitle("Sistema de Agendamento")
janela.resize(300,600)

label_nome =  QLabel("Digite seu nome : ")
label_nome.setStyleSheet('font-weight:bold;margin-top:5px;')

nome =  QLineEdit()

label_calendario =  QLabel("Escolha a data de agendamento : ")
label_calendario.setStyleSheet('font-weight:bold;margin-top:5px;')

calendario =  QCalendarWidget()

botao_enviar =  QPushButton("Enviar")

layout =  QVBoxLayout()
layout.addWidget(label_nome)
layout.addWidget(nome)
layout.addWidget(label_calendario)
layout.addWidget(calendario)
layout.addWidget(botao_enviar)

janela.setLayout(layout)
janela.show()

aplicativo.exec()