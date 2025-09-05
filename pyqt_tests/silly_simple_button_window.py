import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A Silly Simple Applcation")
        button = QPushButton("Push the big shiny button!")
        self.setFixedSize(QSize(700, 600))
        button.setFixedSize(QSize(200,300))
        self.setCentralWidget(button)
        button.clicked.connect(self.close)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()