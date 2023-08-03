from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


app = QApplication([])
main_window = QWidget()


text = QLabel('натисни щоб дізнатися переможця')
winer = QLabel('?')
button = QPushButton('Згенерувати')

line = QVBoxLayout()
line.addWidget(button, alignment= Qt.AlignCenter )
line.addWidget(text, alignment= Qt.AlignCenter)
line.addWidget(winer, alignment= Qt.AlignCenter)

main_window.setLayout(line)

def win():
    ran = randint(1,1000)
    winer.setText(str(ran))

button.clicked.connect(win)

main_window.show()
app.exec_()


