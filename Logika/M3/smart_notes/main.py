from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, 
    QHBoxLayout, QVBoxLayout, QListWidget, QLineEdit, 
    QTextEdit, QInputDialog, QTableWidget,  QListWidgetItem,
    QFormLayout, QGroupBox, QButtonGroup, QRadioButton, QSpinBox)
import json

def writeToFile():
    with open('note.json','w',encoding='utf8')as file:
        json.dump(note,file,ensure_ascii=False,sort_keys=True,indent=4)

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
field_tag = QLineEdit()

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
col2.addWidget(field_tag)
col2.addLayout(row2)
col2.addWidget(btn_search)



with open('note.json','r',encoding = 'utf-8')as file:
    note = json.load(file)



def show_note():
    key = lst_notes.currentItem().text()
    field_text.setText(note[key]['текст'])
    
    lst_tags.clear()
    lst_tags.addItems(note[key]['теги'])

def add_note():
    note_name,ok = QInputDialog.getText(window,'Додати замітку','Назва замітки')

    if note_name and ok:
        note[note_name] = {'текст': '', 'теги': []}
        lst_notes.addItem(note_name)

def save_note():
    if lst_notes.currentItem():
        key = lst_notes.currentItem().text()
        note[key]['текст'] = field_text.toPlainText()
        
        writeToFile()

def del_note():
    if lst_notes.currentItem():
        key = lst_notes.currentItem().text()
        del note[key]

        field_text.clear()
        lst_tags.clear()
        lst_notes.clear()

        lst_notes.addItem(note)
        writeToFile()


def add_tag():
    if lst_notes.currentItem():
        key = lst_notes.currentItem().text()
        tag = field_tag.text()

    note[key]['теги'].append(tag)
    

    lst_tags.addItem(tag)
    field_tag.clear()

    writeToFile()

def del_tag():
    key = lst_notes.currentItem().text()
    tag = lst_tags.currentItem().text()

    note[key]['теги'].remove(tag)

    lst_tags.addItem(note[key]['теги'])
    field_tag.clear()

    writeToFile()

def search_tag():
    tag = field_tag.text()
    if btn_search.text() == 'пошук по тегу':
        filtreted_notes = {} 
    
        for key in note:
            if tag in note[key]['теги']:
                filtreted_notes[key] = note[key]

        btn_search.setText('скинути пошук')

        lst_notes.clear()
        lst_notes.addItems(filtreted_notes)

        lst_tags.clear()
    elif btn_search.text() == 'скинути пошук':
        btn_search.setText('пошук по тегу')

        field_text.clear()
        lst_notes.clear()
        lst_tags.clear()
        field_tag.clear()

        lst_notes.addItems(note)

btn_add.clicked.connect(add_tag)
btn_unfasten.clicked.connect(del_tag)
btn_search.clicked.connect(search_tag)

lst_notes.itemClicked.connect(show_note)

btn_creat.clicked.connect(add_note)
btn_unfasten.clicked.connect(add_note)


lst_notes.addItems(note)
window.setLayout(layout_notes)
window.show()
app.exec_()