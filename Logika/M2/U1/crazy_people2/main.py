from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,QRadioButton, QHBoxLayout, QMessageBox


app = QApplication([])
main_window = QWidget()

Labale = QLabel('коли була створена перша машина?')


def lose():
    b = QMessageBox()
    b.setText('не правильно')
    b.exec_()

def win():
    b = QMessageBox()
    b.setText('Правильно')
    b.exec_()

radio_btn1 = QRadioButton('1887')
radio_btn2 = QRadioButton('1873')
radio_btn3 = QRadioButton('1866')
radio_btn4 = QRadioButton('1892')

a = QVBoxLayout()
a1 = QHBoxLayout()
a2 = QHBoxLayout()
a3 = QHBoxLayout()

a1.addWidget(Labale,alignment=Qt.AlignCenter)
a2.addWidget(radio_btn1,alignment=Qt.AlignCenter)
a2.addWidget(radio_btn2,alignment=Qt.AlignCenter)
a3.addWidget(radio_btn3,alignment=Qt.AlignCenter)
a3.addWidget(radio_btn4,alignment=Qt.AlignCenter)

a.addLayout(a1)
a.addLayout(a2)
a.addLayout(a3)

main_window.setLayout(a)

main_window.show()
app.exec_() 