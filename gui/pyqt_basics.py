
from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QHBoxLayout, QLineEdit, QVBoxLayout, QGridLayout, \
    QFormLayout


def hello():
    name = edit.text()
    print(f"Hello, {name}!")


app = QApplication([])

form = QDialog()

edit = QLineEdit()

button = QPushButton("Hello")
button.clicked.connect(hello)

# layout = QHBoxLayout()  # horizontal layout
# layout = QVBoxLayout()  # vertical layout
# layout = QGridLayout()  # grid layout
# layout.addWidget(edit, 0, 0, 1, -1)
# layout.addWidget(button, 1, 1)

layout = QFormLayout()
layout.addRow("Name: ", edit)
layout.addRow(button)

form.setLayout(layout)
form.show()

app.exec_()
