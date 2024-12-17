

import sys
from PyQt5.QtCore import QRect, QSize, QMetaObject, QCoreApplication
from cinema_menu2 import Ui_menu

from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QLabel, QMessageBox, QMainWindow, QWidget
from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication
from PyQt5.QtGui import QFont
from registration_cinema import Ui_Registration
from admin import Ui_Admin
import requests


class Ui_Login:
    def setupUi(self, Login):
        self.login_window = Login
        Login.setObjectName("Login")
        Login.resize(976, 792)
        Login.setMaximumSize(QSize(1563, 16777215))
        Login.setStyleSheet("")
        self.widget = QWidget(Login)
        self.widget.setGeometry(QRect(20, 20, 951, 761))
        self.widget.setObjectName("widget")
        self.label = QLabel(self.widget)
        self.label.setGeometry(QRect(0, 0, 941, 751))
        self.label.setStyleSheet("background-image: url(images/picture.jpeg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QLabel(self.widget)
        self.label_2.setGeometry(QRect(0, 0, 941, 751))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(self.widget)
        self.label_3.setGeometry(QRect(290, 110, 381, 571))
        self.label_3.setStyleSheet("background-color: rgba(0, 0, 0, 0.7);\n"
                "    border-radius: 8px;\n"
                "")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QLabel(self.widget)
        self.label_4.setGeometry(QRect(420, 160, 121, 41))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("    margin-block-start: 0;\n"
                "    margin-block-end: 0;\n"
                "    margin: 0;\n"
                "    padding: 0;\n"
                "    color: rgb(255, 255, 255);\n"
                "    font-size: 2rem;\n"
                "    font-weight: 700;")
        self.label_4.setObjectName("label_4")
        self.lineEdit_userName = QLineEdit(self.widget)
        self.lineEdit_userName.setGeometry(QRect(380, 250, 201, 41))
        font = QFont()
        font.setPointSize(12)
        self.lineEdit_userName.setFont(font)
        self.lineEdit_userName.setStyleSheet("QLineEdit {\n"
                "    background-color: rgba(0, 0, 0, 0);\n"
                "    border: none;\n"
                "    border-bottom: 2px solid rgba(105, 118, 132, 255);\n"
                "    color: rgb(255, 255, 255);\n"
                "    padding-bottom: 7px;\n"
                "}\n"
                "\n"
                "QLineEdit::placeholder {\n"
                "    color: rgb(255, 255, 255);  /* Placeholder text color */  /* Placeholder text size */\n"
                "}\n"
                "")
        self.lineEdit_userName.setObjectName("lineEdit_userName")
        self.lineEdit_userName_2 =QLineEdit(self.widget)
        self.lineEdit_userName_2.setGeometry(QRect(380, 340, 201, 41))
        self.lineEdit_userName_2.setEchoMode(QLineEdit.Password)
        font = QFont()
        font.setPointSize(12)
        self.lineEdit_userName_2.setFont(font)
        self.lineEdit_userName_2.setStyleSheet("QLineEdit {\n"
                "    background-color: rgba(0, 0, 0, 0);\n"
                "    border: none;\n"
                "    border-bottom: 2px solid rgba(105, 118, 132, 255);\n"
                "    color: rgb(255, 255, 255);\n"
                "    padding-bottom: 7px;\n"
                "}\n"
                "\n"
                "QLineEdit::placeholder {\n"
                "    color: rgb(255, 255, 255);  /* Placeholder text color */  /* Placeholder text size */\n"
                "}\n"
                "")
        self.lineEdit_userName_2.setObjectName("lineEdit_userName_2")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setGeometry(QRect(380, 450, 201, 51))
        font = QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
                "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
                " color:rgba(255, 255, 255, 210);\n"
                " border-radius:5px;\n"
                "}\n"
                "QPushButton#pushButton:hover{   \n"
                " background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0            rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
                "}\n"
                "QPushButton#pushButton:pressed{    \n"
                " padding-left:5px;\n"
                "padding-top:5px;\n"
                "    background-color:rgba(105, 118, 132, 200);\n"
                "}\n"
                "")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setGeometry(QRect(380, 530, 201, 51))
        font = QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2{\n"
                "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
                " color:rgba(255, 255, 255, 210);\n"
                " border-radius:5px;\n"
                "}\n"
                "QPushButton#pushButton_2:hover{   \n"
                " background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0            rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
                "}\n"
                "QPushButton#pushButton_2:pressed{    \n"
                " padding-left:5px;\n"
                "padding-top:5px;\n"
                "    background-color:rgba(105, 118, 132, 200);\n"
                "}\n"
                "")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Login)
        QMetaObject.connectSlotsByName(Login)


    def retranslateUi(self, Login):
        _translate = QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Dialog"))
        self.label_4.setText(_translate("Login", "MOVEAIT"))
        self.lineEdit_userName.setPlaceholderText(_translate("Login", "User Name"))
        self.lineEdit_userName_2.setPlaceholderText(_translate("Login", "Password"))
        self.pushButton.setText(_translate("Login", "E n t e r"))
        self.pushButton_2.setText(_translate("Login", "R e g i s t e r"))

        self.pushButton_2.clicked.connect(self.clicked_to_to_register)
        self.pushButton.clicked.connect(self.login)


    def login(self):
        username = self.lineEdit_userName.text()
        password = self.lineEdit_userName_2.text()

        # Check if the user is an admin
        if (username == "admin" or username == "Jumu") and password == "123":
            self.login_window.close()
            admin_window = QDialog()
            admin_ui = Ui_Admin()  # Pass Cinema instance to the Admin UI
            admin_ui.setupUi(admin_window)
            admin_window.exec()
        else:
            # Check if the user exists in the remote clients dictionary
            url = f"https://aiatulla.pythonanywhere.com/checkuser"
            
            try:
                response = requests.get(url,params={"name":username,"password":password})
                if response.status_code == 200:
                    data = response.json()
                    self.login_window.close()  # Close the login window
                    user_menu = QDialog()  # Create the user menu window
                    user_ui = Ui_menu(username, password)  # Pass Cinema instance
                    user_ui.setupUi(user_menu)
                    user_menu.exec()
                else:
                    QMessageBox.warning(self, "User Not Found")

                # elif response.status_code == 404:
                #     data = response.json()
                #     QMessageBox.warning(self, "User Not Found", data["message"])
                # else:
                #     QMessageBox.critical(self, "Error", f"Unexpected error: {response.text}")
            except requests.ConnectionError:
                QMessageBox.critical(self, "Connection Error", "Failed to connect to the server. Ensure the Flask app is running.")



        
    
    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()


    def clicked_to_to_register(self):
        self.login_window.close()
        registration_window = QDialog()  
        ui = Ui_Registration()  # Pass the Cinema object or instance
        ui.setupUi(registration_window) 
        registration_window.exec()




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Login = QDialog()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
