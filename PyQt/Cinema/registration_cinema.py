
# from PyQt5.QtCore import QRect, QSize, QMetaObject, QCoreApplication
# from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QLabel, QMessageBox, QWidget
# from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication
# from PyQt5.QtGui import QFont
# import requests


# class Ui_Registration:
#     def setupUi(self, Registration):
#         self.Registration = Registration
#         Registration.setObjectName("Registration")
#         Registration.resize(441, 575)
#         Registration.setStyleSheet("border-radius:30px;\n"
# "")
#         self.widget_2 = QWidget(Registration)
#         self.widget_2.setGeometry(QRect(10, 10, 431, 561))
#         self.widget_2.setObjectName("widget_2")
#         self.pushButton_3 = QPushButton(self.widget_2)
#         self.pushButton_3.setGeometry(QRect(90, 440, 191, 51))
#         self.pushButton_3.setSizeIncrement(QSize(380, 470))
#         font = QFont()
#         font.setPointSize(12)
#         self.pushButton_3.setFont(font)
#         self.pushButton_3.setStyleSheet("QPushButton#pushButton_3{\n"
#                 "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
#                 " color:rgba(255, 255, 255, 210);\n"
#                 " border-radius:5px;\n"
#                 "}\n"
#                 "QPushButton#pushButton_3:hover{   \n"
#                 " background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0            rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
#                 "}\n"
#                 "QPushButton#pushButton_3:pressed{    \n"
#                 " padding-left:5px;\n"
#                 "padding-top:5px;\n"
#                 "    background-color:rgba(105, 118, 132, 200);\n"
#                 "}")
#         self.pushButton_3.setObjectName("pushButton_3")
#         self.label = QLabel(self.widget_2)
#         self.label.setGeometry(QRect(30, 60, 151, 41))
#         self.label.setSizeIncrement(QSize(0, 0))
#         font = QFont()
#         font.setPointSize(15)
#         self.label.setFont(font)
#         self.label.setStyleSheet("color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));")
#         self.label.setObjectName("label")
#         self.pushButton_4 = QPushButton(self.widget_2)
#         self.pushButton_4.setGeometry(QRect(290, 20, 111, 41))
#         self.pushButton_4.setSizeIncrement(QSize(380, 470))
#         font = QFont()
#         font.setPointSize(12)
#         self.pushButton_4.setFont(font)
#         self.pushButton_4.setStyleSheet("QPushButton#pushButton_4{\n"
#                 "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
#                 " color:rgba(255, 255, 255, 210);\n"
#                 " border-radius:5px;\n"
#                 "}\n"
#                 "QPushButton#pushButton_4:hover{   \n"
#                 " background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0            rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
#                 "}\n"
#                 "QPushButton#pushButton_4:pressed{    \n"
#                 " padding-left:5px;\n"
#                 "padding-top:5px;\n"
#                 "    background-color:rgba(105, 118, 132, 200);\n"
#                 "}")
#         self.pushButton_4.setObjectName("pushButton_4")
#         self.lineEdit = QLineEdit(self.widget_2)
#         self.lineEdit.setGeometry(QRect(90, 250, 191, 26))
#         self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);border:none;border-bottom:2px solid rgba(105,118,132, 255);\n"
#                 "color:rbga(255, 255, 255,230);padding-bottom:7px;")
#         self.lineEdit.setObjectName("lineEdit")
#         self.lineEdit_2 = QLineEdit(self.widget_2)
#         self.lineEdit_2.setGeometry(QRect(90, 310, 191, 26))
#         self.lineEdit_2.setStyleSheet("background-color:rgba(0,0,0,0);border:none;border-bottom:2px solid rgba(105,118,132, 255);\n"
#                 "color:rbga(255, 255, 255,230);padding-bottom:7px;")
#         self.lineEdit_2.setObjectName("lineEdit_2")
#         self.lineEdit_2.setEchoMode(QLineEdit.Password)

#         self.lineEdit_3 = QLineEdit(self.widget_2)
#         self.lineEdit_3.setGeometry(QRect(90, 370, 191, 26))
#         self.lineEdit_3.setStyleSheet("background-color:rgba(0,0,0,0);border:none;border-bottom:2px solid rgba(105,118,132, 255);\n"
#                 "color:rbga(255, 255, 255,230);padding-bottom:7px;")
#         self.lineEdit_3.setObjectName("lineEdit_3")
#         self.lineEdit_3.setEchoMode(QLineEdit.Password)

#         self.retranslateUi(Registration)
#         QMetaObject.connectSlotsByName(Registration)

#     def retranslateUi(self, Registration):
#         _translate = QCoreApplication.translate
#         Registration.setWindowTitle(_translate("Registration", "Dialog"))
#         self.pushButton_3.setText(_translate("Registration", "R e g i s t r a t i o n"))
#         self.label.setText(_translate("Registration", "Registration"))
#         self.pushButton_4.setText(_translate("Registration", "B a c k"))
#         self.lineEdit.setPlaceholderText(_translate("Registration", "User Name"))
#         self.lineEdit_2.setPlaceholderText(_translate("Registration", "Password"))
#         self.lineEdit_3.setPlaceholderText(_translate("Registration", "Verify password"))

#         self.pushButton_4.clicked.connect(self.back_to_login)
#         self.pushButton_3.clicked.connect(self.registration)

#     def registration(self):
#         name = self.lineEdit.text()
#         password = self.lineEdit_2.text()
#         verify_pass = self.lineEdit_3.text()
#         url = "https://aiatulla.pythonanywhere.com/addclient"
#         if password == verify_pass:
#                 params = {"username": name, "password": password}
#                 try:
#                     response = requests.post(url, params=params)
#                     if response.status_code == 200:
#                         QMessageBox.information(self.Registration, "REGISTRATION", "Successfully registered!", QMessageBox.Ok)
#                     elif response.status_code == 409:  # Example: Handle conflict error for existing user
#                         QMessageBox.warning(self.Registration, "REGISTRATION", "User already exists!", QMessageBox.Ok)
#                     else:
#                         QMessageBox.warning(self.Registration, "REGISTRATION", f"Error: {response.status_code}", QMessageBox.Ok)
#                 except requests.exceptions.RequestException as e:
#                         QMessageBox.critical(self.Registration, "REGISTRATION", f"Network error: {e}", QMessageBox.Ok)

#         else:
#             QMessageBox.warning(self.Registration, "REGISTRATION", "Passwords do not match!", QMessageBox.Ok)

             
#     def back_to_login(self):
#         from login_cinema import Ui_Login
#         self.Registration.close()
#         login_window = QDialog()
#         ui = Ui_Login()  
#         ui.setupUi(login_window)
#         login_window.exec()



# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     Registration =QDialog()
#     ui = Ui_Registration()
#     ui.setupUi(Registration)
#     Registration.show()
#     sys.exit(app.exec_())



#2 


from PyQt5.QtCore import QRect, QSize, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QLabel, QMessageBox, QWidget
from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication
from PyQt5.QtGui import QFont
import requests


class Ui_Registration:
    def setupUi(self, Registration):
        self.Registration = Registration
        Registration.setObjectName("Registration")
        Registration.resize(441, 575)
        Registration.setStyleSheet("border-radius:30px;\n"
"")
        self.widget_2 = QWidget(Registration)
        self.widget_2.setGeometry(QRect(10, 10, 431, 561))
        self.widget_2.setObjectName("widget_2")
        self.pushButton_3 = QPushButton(self.widget_2)
        self.pushButton_3.setGeometry(QRect(90, 440, 191, 51))
        self.pushButton_3.setSizeIncrement(QSize(380, 470))
        font = QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton#pushButton_3{\n"
                "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
                " color:rgba(255, 255, 255, 210);\n"
                " border-radius:5px;\n"
                "}\n"
                "QPushButton#pushButton_3:hover{   \n"
                " background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0            rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
                "}\n"
                "QPushButton#pushButton_3:pressed{    \n"
                " padding-left:5px;\n"
                "padding-top:5px;\n"
                "    background-color:rgba(105, 118, 132, 200);\n"
                "}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QLabel(self.widget_2)
        self.label.setGeometry(QRect(30, 60, 151, 41))
        self.label.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));")
        self.label.setObjectName("label")
        self.pushButton_4 = QPushButton(self.widget_2)
        self.pushButton_4.setGeometry(QRect(290, 20, 111, 41))
        self.pushButton_4.setSizeIncrement(QSize(380, 470))
        font = QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4{\n"
                "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
                " color:rgba(255, 255, 255, 210);\n"
                " border-radius:5px;\n"
                "}\n"
                "QPushButton#pushButton_4:hover{   \n"
                " background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0            rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
                "}\n"
                "QPushButton#pushButton_4:pressed{    \n"
                " padding-left:5px;\n"
                "padding-top:5px;\n"
                "    background-color:rgba(105, 118, 132, 200);\n"
                "}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QRect(90, 250, 191, 26))
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);border:none;border-bottom:2px solid rgba(105,118,132, 255);\n"
                "color:rbga(255, 255, 255,230);padding-bottom:7px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QLineEdit(self.widget_2)
        self.lineEdit_2.setGeometry(QRect(90, 310, 191, 26))
        self.lineEdit_2.setStyleSheet("background-color:rgba(0,0,0,0);border:none;border-bottom:2px solid rgba(105,118,132, 255);\n"
                "color:rbga(255, 255, 255,230);padding-bottom:7px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.lineEdit_3 = QLineEdit(self.widget_2)
        self.lineEdit_3.setGeometry(QRect(90, 370, 191, 26))
        self.lineEdit_3.setStyleSheet("background-color:rgba(0,0,0,0);border:none;border-bottom:2px solid rgba(105,118,132, 255);\n"
                "color:rbga(255, 255, 255,230);padding-bottom:7px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setEchoMode(QLineEdit.Password)

        self.retranslateUi(Registration)
        QMetaObject.connectSlotsByName(Registration)

    def retranslateUi(self, Registration):
        _translate = QCoreApplication.translate
        Registration.setWindowTitle(_translate("Registration", "Dialog"))
        self.pushButton_3.setText(_translate("Registration", "R e g i s t r a t i o n"))
        self.label.setText(_translate("Registration", "Registration"))
        self.pushButton_4.setText(_translate("Registration", "B a c k"))
        self.lineEdit.setPlaceholderText(_translate("Registration", "User Name"))
        self.lineEdit_2.setPlaceholderText(_translate("Registration", "Password"))
        self.lineEdit_3.setPlaceholderText(_translate("Registration", "Verify password"))

        self.pushButton_4.clicked.connect(self.back_to_login)
        self.pushButton_3.clicked.connect(self.registration)

    # def registration(self):
    #     name = self.lineEdit.text()
    #     password = self.lineEdit_2.text()
    #     verify_pass = self.lineEdit_3.text()
    #     url = "https://aiatulla.pythonanywhere.com/addclient"
    #     if password == verify_pass:
    #             params = {"username": name, "password": password}
    #             try:
    #                 response = requests.post(url, params=params)
    #                 if response.status_code == 200:
    #                     QMessageBox.information(self.Registration, "REGISTRATION", "Successfully registered!", QMessageBox.Ok)
    #                 elif response.status_code == 409:  # Example: Handle conflict error for existing user
    #                     QMessageBox.warning(self.Registration, "REGISTRATION", "User already exists!", QMessageBox.Ok)
    #                 else:
    #                     QMessageBox.warning(self.Registration, "REGISTRATION", f"Error: {response.status_code}", QMessageBox.Ok)
    #             except requests.exceptions.RequestException as e:
    #                     QMessageBox.critical(self.Registration, "REGISTRATION", f"Network error: {e}", QMessageBox.Ok)

    #     else:
    #         QMessageBox.warning(self.Registration, "REGISTRATION", "Passwords do not match!", QMessageBox.Ok)

    def registration(self):
        name = self.lineEdit.text()
        password = self.lineEdit_2.text()
        verify_pass = self.lineEdit_3.text()
        url = "https://aiatulla.pythonanywhere.com/addclient"
        if password == verify_pass:
            params = {"username": name, "password": password}
            try:
                response = requests.post(url, json=params)  # Use `json` for JSON data
                if response.status_code == 200:
                    QMessageBox.information(self.Registration, "REGISTRATION", "Successfully registered!", QMessageBox.Ok)
                elif response.status_code == 409:  # Conflict error for existing user
                    QMessageBox.warning(self.Registration, "REGISTRATION", "User already exists!", QMessageBox.Ok)
                else:
                    QMessageBox.warning(self.Registration, "REGISTRATION", f"Error: {response.status_code}", QMessageBox.Ok)
            except requests.exceptions.RequestException as e:
                QMessageBox.critical(self.Registration, "REGISTRATION", f"Network error: {e}", QMessageBox.Ok)
        else:
            QMessageBox.warning(self.Registration, "REGISTRATION", "Passwords do not match!", QMessageBox.Ok)

   
    def back_to_login(self):
        from login_cinema import Ui_Login
        self.Registration.close()
        login_window = QDialog()
        ui = Ui_Login()  
        ui.setupUi(login_window)
        login_window.exec()



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Registration =QDialog()
    ui = Ui_Registration()
    ui.setupUi(Registration)
    Registration.show()
    sys.exit(app.exec_())
