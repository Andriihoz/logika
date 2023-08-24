''' Вікно для картки питання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox,)
app = QApplication([])

# віджети, які треба буде розмістити:
# кнопка повернення в основне вікно 
btn_menu = QPushButton('Меню')
# кнопка прибирає вікно і повертає його після закінчення таймера
btn_sleep = QPushButton('Відпочити')
btn_OK = QPushButton('Відповісти')
lb_Question = QLabel()

box_minuts = QSpinBox()
box_minuts.setValue(5)

RadioGroupBox = QGroupBox('Варіанти відповідей')
RadioGroup = QButtonGroup()


rbtn1 = QRadioButton('')
rbtn2 = QRadioButton('')
rbtn3 = QRadioButton('')
rbtn4 = QRadioButton('')


RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)


layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат тесту')
lb_Results = QLabel('')
lb_Correct = QLabel('')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Results,aligment=(Qt.Aligment | Qt.Alignment))
layout_res.addWidget(lb_Correct,aligment=Qt.AlignHCentr)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()
def show_result():

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_menu)
layout_line1.addWidget(1)
layout_line1.addWidget(btn_sleep)
layout_line1.addWidget(box_minuts)
layout_line1.addWidget(QLabel('хвилин'))

layout_line2.addWidget(lb_Results,aligment=(Qt.Aligment | Qt.Alignment))

layout_line3.addWidget(RadioGroupBox)
layout_line3.addStretch(AnsGroupBox)

layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK)
layout_line4.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1,stretch=1)
layout_card.addLayout(layout_line2,stretch=2)
layout_card.addLayout(layout_line3,stretch=3)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4,st)
layout_card.addStretch(1)
layout_card.addStretch(5)

    ''' показати панель відповідей '''
    pass

def show_question():
    ''' показати панель запитань '''
    pass


