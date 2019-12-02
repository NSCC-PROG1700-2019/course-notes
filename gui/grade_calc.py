
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QLabel, QLineEdit, QGroupBox, QHBoxLayout, QVBoxLayout, \
    QFrame, QPushButton


def calc_grade(mark, total):
    return round(mark / total * 100.0, 1)


def get_assignment_grade(index):
    return int(assignment_grade[index].text()), \
            int(assignment_total[index].text())


def get_assignment_grades():
    grades = []
    for idx, _ in enumerate(assignment_grade):
        grades.append(get_assignment_grade(idx))
    grades.sort(key=lambda x: x[0])
    grades.pop(0)
    return grades


def display_assignment_grades():
    for p, (m, t) in zip(assignment_prcnt, get_assignment_grades()):
        p.setText(f'{calc_grade(m, t)}%')


def calcbutton_clicked():
    get_assignment_grades()
    display_assignment_grades()


app = QApplication([])

form = QDialog()
form.setWindowTitle('Grade Master 5000')

# assignments
assignment_gridlayout = QGridLayout()

assignment_label = []
assignment_grade = []
assignment_slash = []
assignment_total = []
assignment_prcnt = []
for i in range(5):
    assignment_label.append(QLabel(f'Assignment {i+1}:'))
    assignment_grade.append(QLineEdit())
    assignment_slash.append(QLabel('/'))
    assignment_total.append(QLineEdit())
    assignment_prcnt.append(QLabel('100%'))

    assignment_gridlayout.addWidget(assignment_label[i], i, 0)
    assignment_gridlayout.addWidget(assignment_grade[i], i, 1)
    assignment_gridlayout.addWidget(assignment_slash[i], i, 2)
    assignment_gridlayout.addWidget(assignment_total[i], i, 3)
    assignment_gridlayout.addWidget(assignment_prcnt[i], i, 4)

assignment_groupbox = QGroupBox('Assignments')
assignment_groupbox.setLayout(assignment_gridlayout)

# project
project_label = QLabel('Final Project')
project_grade = QLineEdit()
project_slash = QLabel('/')
project_total = QLineEdit()
project_prcnt = QLabel('100%')

project_layout = QHBoxLayout()
project_layout.addWidget(project_label)
project_layout.addWidget(project_grade)
project_layout.addWidget(project_slash)
project_layout.addWidget(project_total)
project_layout.addWidget(project_prcnt)

project_groupbox = QGroupBox('Projects')
project_groupbox.setLayout(project_layout)

# grade calculations
finalgrade_title_label = QLabel('Final Grade')
finalgrade_title_label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
finalgrade_title_label.setFont(QFont('Arial', 18, QFont.Bold))
finalgrade_title_label.setStyleSheet('color: white')
finalgrade_value_label = QLabel('100%')
finalgrade_value_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
finalgrade_value_label.setFont(QFont('Arial', 18))
finalgrade_value_label.setStyleSheet('color: white')

finalgrade_layout = QVBoxLayout()
finalgrade_layout.addWidget(finalgrade_title_label)
finalgrade_layout.addWidget(finalgrade_value_label)

finalgrade_frame = QFrame()
finalgrade_frame.setStyleSheet('background-color: green')
finalgrade_frame.setFrameStyle(QFrame.Box | QFrame.Plain)
finalgrade_frame.setLineWidth(2)
finalgrade_frame.setLayout(finalgrade_layout)

maxgrade_title_label = QLabel('Max Grade')
maxgrade_title_label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
maxgrade_title_label.setFont(QFont('Arial', 18, QFont.Bold))
maxgrade_title_label.setStyleSheet('color: white')
maxgrade_value_label = QLabel('100%')
maxgrade_value_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
maxgrade_value_label.setFont(QFont('Arial', 18))
maxgrade_value_label.setStyleSheet('color: white')

maxgrade_layout = QVBoxLayout()
maxgrade_layout.addWidget(maxgrade_title_label)
maxgrade_layout.addWidget(maxgrade_value_label)

maxgrade_frame = QFrame()
maxgrade_frame.setStyleSheet('background-color: gray')
maxgrade_frame.setFrameStyle(QFrame.Box | QFrame.Plain)
maxgrade_frame.setLineWidth(1)
maxgrade_frame.setLayout(maxgrade_layout)

avggrade_title_label = QLabel('Avg Grade')
avggrade_title_label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
avggrade_title_label.setFont(QFont('Arial', 18, QFont.Bold))
avggrade_title_label.setStyleSheet('color: white')
avggrade_value_label = QLabel('100%')
avggrade_value_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
avggrade_value_label.setFont(QFont('Arial', 18))
avggrade_value_label.setStyleSheet('color: white')

avggrade_layout = QVBoxLayout()
avggrade_layout.addWidget(avggrade_title_label)
avggrade_layout.addWidget(avggrade_value_label)

avggrade_frame = QFrame()
avggrade_frame.setStyleSheet('background-color: gray')
avggrade_frame.setFrameStyle(QFrame.Box | QFrame.Plain)
avggrade_frame.setLineWidth(1)
avggrade_frame.setLayout(avggrade_layout)

mingrade_title_label = QLabel('Min Grade')
mingrade_title_label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
mingrade_title_label.setFont(QFont('Arial', 18, QFont.Bold))
mingrade_title_label.setStyleSheet('color: white')
mingrade_value_label = QLabel('100%')
mingrade_value_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
mingrade_value_label.setFont(QFont('Arial', 18))
mingrade_value_label.setStyleSheet('color: white')

mingrade_layout = QVBoxLayout()
mingrade_layout.addWidget(mingrade_title_label)
mingrade_layout.addWidget(mingrade_value_label)

mingrade_frame = QFrame()
mingrade_frame.setStyleSheet('background-color: gray')
mingrade_frame.setFrameStyle(QFrame.Box | QFrame.Plain)
mingrade_frame.setLineWidth(1)
mingrade_frame.setLayout(mingrade_layout)

# buttons

load_button = QPushButton('Load')
save_button = QPushButton('Save')
calc_button = QPushButton('Calculate')
calc_button.clicked.connect(calcbutton_clicked)
exit_button = QPushButton('Exit')

button_layout = QHBoxLayout()
button_layout.setSpacing(5)
button_layout.addWidget(load_button)
button_layout.addWidget(save_button)
button_layout.addWidget(calc_button)
button_layout.addWidget(exit_button)

# final layout
layout = QGridLayout()
layout.addWidget(assignment_groupbox, 0, 0, 3, 2)
layout.addWidget(project_groupbox, 3, 0, 1, 2)
layout.addWidget(finalgrade_frame, 0, 2)
layout.addWidget(maxgrade_frame, 1, 2)
layout.addWidget(avggrade_frame, 2, 2)
layout.addWidget(mingrade_frame, 3, 2)
# layout.addItem(mingrade_layout, 3, 2)
layout.addItem(button_layout, 4, 1, 1, 2)

form.setLayout(layout)
form.show()
app.exec_()
