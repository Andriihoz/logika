from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, 
    QHBoxLayout, QVBoxLayout, QListWidget, QLineEdit, 
    QTextEdit, QInputDialog, QTableWidget,  QListWidgetItem,
    QFormLayout, QGroupBox, QButtonGroup, QRadioButton, QSpinBox)
import json


app = QApplication([])
window = QWidget()


field_text = QTextEdit()
lb_notes = QLabel('Список заміток')
lst_notes = QListWidget()

btn_notes = QPushButton()

btn_creat = QPushButton('Створити замітку')
btn_delete = QPushButton('Видалити замітку')
btn_save = QPushButton('Зберегти замітку')

lb_tags = QLabel('Спмсрк тегів')
lst_tags = QListWidget()

btn_add = QPushButton('Додати до замітки')
btn_unfasten = QPushButton('Відкріпити від замітки')
btn_search = QPushButton('Шукати замітки за тегом')

layout_notes = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

layout_notes.addLayout(col1)
layout_notes.addLayout(col2)

col1.addWidget(field_text)
col2.addWidget(lb_notes)
col2.addWidget(lst_notes)

row1 = QHBoxLayout()
row1.addWidget(btn_creat)
row1.addWidget(btn_delete)

col2.addLayout(row1)

with open('note.json','r',encoding = 'utf-8')as file:
    note = json.load(file)

lst_notes.addItems(note)

window.setLayout(layout_notes)
window.show()
app.exec_()