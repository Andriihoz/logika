from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap 

from PIL import Image, ImageFilter

import os

app = QApplication([])
window = QListWidget()

btn_folder = QPushButton('Папка')
btn_left = QPushButton('Вліво')
btn_right = QPushButton('Вправо')
btn_mirror = QPushButton('Зеркало')
btn_sharpness = QPushButton('Різкість')
btn_BW = QPushButton('Ч/Б')

lst_files = QListWidget()
pic = QLabel('Картина')
layout_editor = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()

row = QHBoxLayout()

col1.addWidget(btn_folder)
col1.addWidget(lst_files)

row.addWidget(btn_left)
row.addWidget(btn_right)
row.addWidget(btn_mirror)
row.addWidget(btn_sharpness)
row.addWidget(btn_BW)

col2.addWidget(pic)
col2.addLayout(row)

layout_editor.addLayout(col1,1)
layout_editor.addLayout(col2,4)

workdir = QFileDialog.getExistingDirectory()

print(workdir)

files = os.listdir(workdir)
print(files)

def filter(filename):
    result = []
    ext = ['jpg','png','jpeg','bmp','gif']

    for file in filename:
        if file.split('.')[-1] in ext:
            result.append(file)
    return result

window.setLayout(layout_editor)
window.show()
app.exec_()