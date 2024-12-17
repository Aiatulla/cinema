

import requests
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Admin(object):
    def setupUi(self, Admin):
        self.admin = Admin
        Admin.setObjectName("Admin")
        Admin.resize(500, 350)

        # Create UI components
        self.pushButton_add_movie = QtWidgets.QPushButton(Admin)
        self.pushButton_add_movie.setGeometry(QtCore.QRect(30, 100, 200, 30))
        self.pushButton_add_movie.setObjectName("pushButton_add_movie")
        self.lineEdit_add_movie = QtWidgets.QLineEdit(Admin)
        self.lineEdit_add_movie.setGeometry(QtCore.QRect(30, 50, 200, 26))
        self.lineEdit_add_movie.setObjectName("lineEdit_add_movie")
        self.pushButton_remove_movie = QtWidgets.QPushButton(Admin)
        self.pushButton_remove_movie.setGeometry(QtCore.QRect(260, 100, 200, 30))
        self.pushButton_remove_movie.setObjectName("pushButton_remove_movie")

        self.lineEdit_movie_for_schedule = QtWidgets.QLineEdit(Admin)
        self.lineEdit_movie_for_schedule.setGeometry(QtCore.QRect(30, 170, 200, 26))
        self.lineEdit_movie_for_schedule.setObjectName("lineEdit_movie_for_schedule")
        self.lineEdit_add_schedule = QtWidgets.QLineEdit(Admin)
        self.lineEdit_add_schedule.setGeometry(QtCore.QRect(260, 170, 200, 26))
        self.lineEdit_add_schedule.setObjectName("lineEdit_add_schedule")
        self.pushButton_add_schedule = QtWidgets.QPushButton(Admin)
        self.pushButton_add_schedule.setGeometry(QtCore.QRect(30, 220, 200, 30))
        self.pushButton_add_schedule.setObjectName("pushButton_add_schedule")
        self.pushButton_remove_schedule = QtWidgets.QPushButton(Admin)
        self.pushButton_remove_schedule.setGeometry(QtCore.QRect(260, 220, 200, 30))
        self.pushButton_remove_schedule.setObjectName("pushButton_remove_schedule")

        self.pushButton_back = QtWidgets.QPushButton(Admin)
        self.pushButton_back.setGeometry(QtCore.QRect(340, 10, 120, 30))
        self.pushButton_back.setObjectName("pushButton_back")

        self.retranslateUi(Admin)
        QtCore.QMetaObject.connectSlotsByName(Admin)

        # Connect buttons to methods
        self.pushButton_add_movie.clicked.connect(self.add_movie)
        self.pushButton_remove_movie.clicked.connect(self.remove_movie)
        self.pushButton_add_schedule.clicked.connect(self.add_schedule)
        self.pushButton_remove_schedule.clicked.connect(self.remove_schedule)
        self.pushButton_back.clicked.connect(self.go_back)

        # Apply styles
        self.apply_styles()

    def retranslateUi(self, Admin):
        _translate = QtCore.QCoreApplication.translate
        Admin.setWindowTitle(_translate("Admin", "Admin Panel"))
        self.pushButton_add_movie.setText(_translate("Admin", "Add Movie"))
        self.lineEdit_add_movie.setPlaceholderText(_translate("Admin", "Enter movie name"))
        self.pushButton_remove_movie.setText(_translate("Admin", "Remove Movie"))
        self.lineEdit_movie_for_schedule.setPlaceholderText(_translate("Admin", "Enter movie name"))
        self.lineEdit_add_schedule.setPlaceholderText(_translate("Admin", "Enter schedule"))
        self.pushButton_add_schedule.setText(_translate("Admin", "Add Schedule"))
        self.pushButton_remove_schedule.setText(_translate("Admin", "Remove Schedule"))
        self.pushButton_back.setText(_translate("Admin", "Back"))

    def apply_styles(self):
        # Basic window style
        self.admin.setStyleSheet("""
            QWidget {
                background-color: #f5f5f5;
                font-family: Arial, sans-serif;
                font-size: 14px;
            }
            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 5px;
                background-color: #ffffff;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: 1px solid #4CAF50;
                border-radius: 5px;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #388e3c;
            }
            QLineEdit:focus {
                border-color: #4CAF50;
            }
            QMessageBox {
                font-family: Arial, sans-serif;
                font-size: 12px;
            }
        """)

    def add_movie(self):
        movie_name = self.lineEdit_add_movie.text().strip()
        if not movie_name:
            QMessageBox.warning(None, "Input Error", "Please enter a movie name!")
            return

        url = "https://aiatulla.pythonanywhere.com/addmovie"
        price = 300  # Example price, this can be dynamically taken as well
        data = {"title": movie_name, "price": price}

        try:
            response = requests.post(url, params=data)  # Using POST method for adding
            response.raise_for_status()
            QMessageBox.information(None, "Success", f"Movie '{movie_name}' added successfully!")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(None, "Error", f"Failed to add movie: {e}")

    def remove_movie(self):
        movie_name = self.lineEdit_add_movie.text().strip()
        if not movie_name:
            QMessageBox.warning(None, "Input Error", "Please enter a movie name to remove!")
            return

        url = "https://aiatulla.pythonanywhere.com/removemovie"
        data = {"title": movie_name}

        try:
            response = requests.get(url, params=data)  # GET method for removing
            response.raise_for_status()
            QMessageBox.information(None, "Success", f"Movie '{movie_name}' removed successfully!")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(None, "Error", f"Failed to remove movie: {e}")

    def add_schedule(self):
        movie_name = self.lineEdit_movie_for_schedule.text().strip()
        schedule = self.lineEdit_add_schedule.text().strip()

        if not movie_name or not schedule:
            QMessageBox.warning(None, "Input Error", "Please enter both movie name and schedule!")
            return

        url = "https://aiatulla.pythonanywhere.com/addschedule"
        data = {"title": movie_name, "schedule": schedule}

        try:
            response = requests.get(url, params=data)  # Using GET for adding schedule
            response.raise_for_status()
            QMessageBox.information(None, "Success", f"Schedule '{schedule}' added for movie '{movie_name}'!")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(None, "Error", f"Failed to add schedule: {e}")

    def remove_schedule(self):
        movie_name = self.lineEdit_movie_for_schedule.text().strip()
        schedule = self.lineEdit_add_schedule.text().strip()

        if not movie_name or not schedule:
            QMessageBox.warning(None, "Input Error", "Please enter both movie name and schedule to remove!")
            return

        url = "https://aiatulla.pythonanywhere.com/removeschedule"
        data = {"title": movie_name, "schedule": schedule}

        try:
            response = requests.get(url, params=data)  # GET method for removing schedule
            response.raise_for_status()
            QMessageBox.information(None, "Success", f"Schedule '{schedule}' removed for movie '{movie_name}'!")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(None, "Error", f"Failed to remove schedule: {e}")

    def go_back(self):
        from login_cinema import Ui_Login
        self.admin.close()
        login_window = QtWidgets.QDialog()
        ui = Ui_Login()  
        ui.setupUi(login_window)
        login_window.exec()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Admin = QtWidgets.QDialog()
    ui = Ui_Admin()
    ui.setupUi(Admin)
    Admin.show()
    sys.exit(app.exec_())
