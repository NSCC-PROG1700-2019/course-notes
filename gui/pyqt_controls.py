
from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QHBoxLayout, QLineEdit, QVBoxLayout, QGridLayout, \
    QFormLayout, QLabel, QComboBox, QCheckBox, QGroupBox, QRadioButton, QListWidget, QMessageBox


def hello():
    msgbox = QMessageBox()
    # QLineEdit
    # name = edit.text()
    # msgbox.setText(f"Hello, {name}!")
    # QComboBox
    # msgbox.setText(combobox.currentText())
    # QCheckBox
    # text = ''
    # if checkbox1.isChecked():
    #     text = "QCheckBox 1!\n"
    # if checkbox2.isChecked():
    #     text += "QCheckBox 2!\n"
    # if text:
    #     msgbox.setText(text)
    # else:
    #     msgbox.setText('No checkbox checked.')
    # QListWidget
    # item = list.currentItem()
    # if item:
    #     text = item.text()
    #     msgbox.setText(text)
    # else:
    #     msgbox.setText('No item selected.')
    msgbox.setWindowTitle('Important Message')
    msgbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    if msgbox.exec() == QMessageBox.Ok:
        list.clear()


app = QApplication([])

form = QDialog()

label = QLabel("QLabel")
edit = QLineEdit("QLineEdit")
button = QPushButton("QPushButton")
button.clicked.connect(hello)
combobox = QComboBox()
combobox.addItem("Item 1")
combobox.addItem("Item 2")

checkbox1 = QCheckBox("QCheckBox 1")
checkbox2 = QCheckBox("QCheckBox 2")
check_groupbox = QGroupBox()
check_layout = QVBoxLayout()
check_layout.addWidget(checkbox1)
check_layout.addWidget(checkbox2)
check_groupbox.setLayout(check_layout)

radio1 = QRadioButton("QRadioButton 1")
radio2 = QRadioButton("QRadioButton 2")
radio_groupbox = QGroupBox()
radio_layout = QVBoxLayout()
radio_layout.addWidget(radio1)
radio_layout.addWidget(radio2)
radio_groupbox.setLayout(radio_layout)

list = QListWidget()
list.addItem("QListItem 1")
list.addItem("QListItem 2")

layout = QGridLayout()
layout.addWidget(label, 0, 0)
layout.addWidget(edit, 0, 1)
layout.addWidget(button, 1, 0)
layout.addWidget(combobox, 1, 1)
layout.addWidget(check_groupbox, 2, 0)
layout.addWidget(radio_groupbox, 2, 1)
layout.addWidget(list, 3, 0, 1, 2)

form.setLayout(layout)
form.show()

app.exec_()
