import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QLabel, QLayout, QWidget


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Landing Page Example")
        self.setGeometry(100, 100, 800, 600)
        self.initUI()


    def initUI(self):
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()