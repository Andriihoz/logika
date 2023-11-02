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


def funk():
    global a
    a = 1
    print(a)

def filter(filename):
    result = []
    ext = ['jpg','png','jpeg','bmp','gif','jfif']

    for file in filename:
        if file.split('.')[-1] in ext:
            result.append(file)
    return result

def showFiles():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    files = os.listdir(workdir)

    grafic_files = filter(files)

    lst_files.clear()
    lst_files.addItems(grafic_files)

class imageProcessor():
    def __init__(self):
        self.original = None
        self.filename = None
        self.save_dir = 'Modified/'

    def load_image(self,filename):
        self.filename = filename
        full_path = os.path.join(workdir,filename)
        self.original = Image.open(full_path)

    def showImage(self,path):
        pic.hide()
        pixmapimage = QPixmap(path)
        w,h = pic.width(), pic.height()
        
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        
        pic.setPixmap(pixmapimage)
        pic.show()
    def saveAndShowImage(self):
        path = os.path.join(workdir,self.save_dir)

        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)

        image_path = os.path.join(path,self.filename) 
        self.original.save(image_path)
        self.showImage(image_path)

    def btn_BW(self):
        self.original = self.original.convert('L')
        self.saveAndShowImage()
    def btn_sharpness(self):
        self.original = self.original.filter(ImageFilter.SHARPEN)
        self.saveAndShowImage()
    def btn_left(self):
        self.original = self.original.transpose(Image.ROTATE_90)
        self.saveAndShowImage()
    def btn_right(self):
        self.original = self.original.transpose(Image.ROTATE_270)
        self.saveAndShowImage()
    def btn_flip(self):
        self.original = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveAndShowImage()

def showChosenItem():
    filename = lst_files.currentItem().text()
    workImage.load_image(filename)
    full_path = os.path.join(workdir,filename)
    workImage.showImage(full_path)

workImage = imageProcessor()

lst_files.itemClicked.connect(showChosenItem)
btn_folder.clicked.connect(showFiles)

btn_BW.clicked.connect(workImage.btn_BW)
btn_left.clicked.connect(workImage.btn_left)
btn_right.clicked.connect(workImage.btn_right)
btn_mirror.clicked.connect(workImage.btn_flip)
btn_sharpness.clicked.connect(workImage.btn_sharpness)

window.resize(900,600)
window.setLayout(layout_editor)
window.show()
app.exec_()