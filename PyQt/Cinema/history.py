


import requests
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_history(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def setupUi(self, Dialog):
        self.history = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(523, 592)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 521, 591))
        self.label.setStyleSheet("background-image: url(images/UserMenu_back.jpeg);\n"
                                 "border-radius:5px;")
        self.label.setText("")
        self.label.setObjectName("label")

        self.pushButton_back = QtWidgets.QPushButton(Dialog)
        self.pushButton_back.setGeometry(QtCore.QRect(320, 20, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setStyleSheet("QPushButton#pushButton_back { /* Styles */ }")
        self.pushButton_back.setObjectName("pushButton_back")

        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancel.setGeometry(QtCore.QRect(130, 510, 241, 41))
        font.setPointSize(12)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setStyleSheet("QPushButton#pushButton_cancel { /* Styles */ }")
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        self.label_user_his = QtWidgets.QLabel(Dialog)
        self.label_user_his.setGeometry(QtCore.QRect(10, 100, 491, 331))
        self.label_user_his.setStyleSheet("background-color:white;")
        self.label_user_his.setText("")
        self.label_user_his.setObjectName("label_user_his")

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 110, 471, 311))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.lineEdit_movie_name = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_movie_name.setGeometry(QtCore.QRect(10, 450, 191, 41))
        self.lineEdit_movie_name.setObjectName("lineEdit_movie_name")
        self.lineEdit_schedule = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_schedule.setGeometry(QtCore.QRect(210, 450, 141, 41))
        self.lineEdit_schedule.setObjectName("lineEdit_schedule")
        self.lineEdit_seat = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_seat.setGeometry(QtCore.QRect(360, 450, 141, 41))
        self.lineEdit_seat.setObjectName("lineEdit_seat")

        self.pushButton_back.clicked.connect(self.back_to_login)
        self.pushButton_cancel.clicked.connect(self.cancel_booking)

        self.display_booking_history()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def back_to_login(self):
        from cinema_menu2 import Ui_menu
        self.history.close()
        menu_window = QtWidgets.QDialog()
        ui = Ui_menu(self.username,self.password)
        ui.setupUi(menu_window)
        menu_window.exec()

    def display_booking_history(self):
        """Fetch and display booking history from Flask server."""
        url = f"https://aiatulla.pythonanywhere.com/viewbookings?username={self.username}&password={self.password}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                bookings = response.text.split("<br>")
                for booking in bookings:
                    label = QtWidgets.QLabel(booking)
                    self.verticalLayout_2.addWidget(label)
            else:
                error_label = QtWidgets.QLabel(response.text)
                self.verticalLayout_2.addWidget(error_label)
        except requests.exceptions.RequestException as e:
            error_label = QtWidgets.QLabel(f"Error connecting to server: {e}")
            self.verticalLayout_2.addWidget(error_label)

    def cancel_booking(self):
        """Cancel a booking via Flask server."""
        url = "https://aiatulla.pythonanywhere.com/cancelbooking"
        data = {
            "username": self.username,
            "password": self.password,
            "title": self.lineEdit_movie_name.text(),
            "schedule": self.lineEdit_schedule.text(),
            "seat": self.lineEdit_seat.text(),
        }
        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                success_label = QtWidgets.QLabel(response.json().get("message", "Booking canceled successfully."))
                self.verticalLayout_2.addWidget(success_label)
            else:
                error_label = QtWidgets.QLabel(response.json().get("error", "Error canceling booking."))
                self.verticalLayout_2.addWidget(error_label)
        except requests.exceptions.RequestException as e:
            error_label = QtWidgets.QLabel(f"Error connecting to server: {e}")
            self.verticalLayout_2.addWidget(error_label)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Booking History"))
        self.pushButton_back.setText(_translate("Dialog", "B a c k"))
        self.pushButton_cancel.setText(_translate("Dialog", "Cancel Booking"))
        self.lineEdit_movie_name.setPlaceholderText(_translate("Dialog", "Movie name"))
        self.lineEdit_schedule.setPlaceholderText(_translate("Dialog", "Schedule"))
        self.lineEdit_seat.setPlaceholderText(_translate("Dialog", "Seat"))



# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_history()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
