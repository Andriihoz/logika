from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, 
    QHBoxLayout, QVBoxLayout, QListWidget, QLineEdit, 
    QTextEdit, QInputDialog, QTableWidget,  QListWidgetItem,
    QFormLayout, QGroupBox, QButtonGroup, QRadioButton, QSpinBox)
import json

def writeToFile():
    with open('note.json','w',encoding='utf8')as file:
        json.dump(note,file,ensure_ascii=False,sort_keys=True,ident=4)

app = QApplication([])
window = QWidget()


field_text = QTextEdit()
lb_notes = QLabel('Список заміток')
lst_notes = QListWidget()

btn_notes = QPushButton()

btn_creat = QPushButton('Створити замітку')
btn_delete = QPushButton('Видалити замітку')
btn_save = QPushButton('Зберегти замітку')

lb_tags = QLabel('Список тегів')
lst_tags = QListWidget()

btn_add = QPushButton('Додати до замітки')
btn_unfasten = QPushButton('Відкріпити від замітки')
btn_search = QPushButton('Шукати замітки за тегом')

layout_notes = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

layout_notes.addLayout(col1, stretch=2)
layout_notes.addLayout(col2, stretch=1)

col1.addWidget(field_text)
col2.addWidget(lb_notes)
col2.addWidget(lst_notes)

row1 = QHBoxLayout()
row1.addWidget(btn_creat)
row1.addWidget(btn_delete)

col2.addLayout(row1)
col2.addWidget(btn_save)

col2.addWidget(lb_tags)
col2.addWidget(lst_tags)

row2 = QHBoxLayout()
row2.addWidget(btn_add)
row2.addWidget(btn_unfasten)

col2.addLayout(row2)
col2.addWidget(btn_search)

col2.addWidget(btn_add)
col2.addWidget(btn_unfasten)

with open('note.json','r',encoding = 'utf-8')as file:
    note = json.load(file)



def show_note():
    key = lst_notes.currentItem().text()
    field_text.setText(note[key]['текст'])
    
    lst_tags.clear()
    lst_tags.addItem(note[key]['теги'])

def add_note():
    note_name,ok = QInputDialog.getText(window,'Додати замітку','Назва замітки')

    if note_name and ok:
        note[note_name] = {'текст': '', 'теги': []}
        lst_notes.addItem(note_name)

def save_note():
    key = lst_notes.currentItem().text()
    note[key]['текст'] = field_text.toPlainText()

def del_note():
    if lst_notes.currentItem():
        key = lst_notes.currentItem().text()
        del note[key]

        field_text.clear()
        lst_tags.clear()
        lst_notes.clear()

        lst_notes.addItem(note)
        writeToFile()

lst_notes.itemClicked.connect(show_note)

btn_creat.clicked.connect(add_note)
btn_unfasten.clicked.connect(add_note)


lst_notes.addItems(note)
window.setLayout(layout_notes)
window.show()
app.exec_()