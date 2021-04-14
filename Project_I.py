from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton)
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Project 1"
        self.top = 100
        self.left = 100
        self.width = 1200
        self.height = 1000

        self.InitWindow()
    
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        button = QPushButton('Pyqt5 button', self)
        button.move(500, 200)
        button.setToolTip('This is the  button')
        self.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
