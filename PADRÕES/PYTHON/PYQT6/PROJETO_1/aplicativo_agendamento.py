#Powered by Linguagem de Máquina using PyQT6
#Resources and documentations : 
# https://www.riverbankcomputing.com/static/Docs/PyQt6/ 

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QPushButton, QLineEdit, QCalendarWidget

# Cria o aplicativo
aplicativo = QApplication(sys.argv)

# Características da janela
# =========================================================

# Define a janela como um widjet
janela =  QWidget()

# Define o título da janela 
janela.setWindowTitle("SISTEMA DE AGENDAMENTO")
# Define o tamanho da janela
janela.resize(300,600)


# Caracteríticas do conteúdo da janela
# =========================================================

# Label de título da seção
label_titulo_secao = QLabel ("SISTEMA DE AGENDAMENTO")
label_titulo_secao.setAlignment(Qt.AlignmentFlag.AlignCenter)
label_titulo_secao.setStyleSheet('font-size:16px; font-weight:bold; margin-top:15px; margin-bottom:15px; color:#3366FF;')



# Label do campo de entrada de dados - nome
label_cpf =  QLabel("DIGITE SEU CPF : ")
label_cpf.setStyleSheet('font-size:12px; font-weight:bold; margin-top:15px; color:#3366FF;')

# Campo de entrada de dados - nome
cpf =  QLineEdit()

# Label do campo de entrada de dados - calendario
label_calendario =  QLabel("Escolha a data de agendamento : ")
label_calendario.setStyleSheet('font-weight:bold; margin-top:15px;')

# Campo de entrada de dados - calendario
calendario =  QCalendarWidget()

# Botão de processamento de dados
# ========================================================

# Define o título do botão
botao_ver_agenda =  QPushButton("VER AGENDA")
# Define um tamanho fixo para o botão
botao_ver_agenda.setFixedWidth(120)



# Define o cursor sobre o botão
botao_ver_agenda.setCursor(QCursor(Qt.CursorShape.ArrowCursor.PointingHandCursor))

# Atribui o CSS aplicável
botao_ver_agenda.setStyleSheet('font-weight:bold; padding:5px; margin-top:15px; margin-bottom:15px; color:#3366FF;')

# Composição do layout
# =========================================================

# Define o layout vertical (VBoxLayout)
layout =  QVBoxLayout()

# Estrutura os elementos de layout
# =========================================================

layout.addWidget(label_titulo_secao)
layout.addWidget(label_cpf)
layout.addWidget(cpf)
layout.addWidget(label_calendario)
layout.addWidget(calendario)
# O parâmetro alignment define a posição do botão
layout.addWidget(botao_ver_agenda, alignment=Qt.AlignmentFlag.AlignCenter)


# Integra o layout montado à janela
janela.setLayout(layout)

# Exibe a janela
janela.show()

# Executa o aplicativo
aplicativo.exec()