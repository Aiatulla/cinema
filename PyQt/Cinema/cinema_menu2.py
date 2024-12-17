
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
import requests

class Ui_menu(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.selected_movie = None
        self.selected_schedule = None
        self.seats_quantity = 0

    def setupUi(self, Dialog):
        self.menu = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(1125, 823)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 1101, 801))
        self.label.setStyleSheet("background-image: url(images/UserMenu_back.jpeg\");")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 1101, 801))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 1061, 691))
        font = QtGui.QFont()
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:white;\n"
"border-radius:5px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 9, 1101, 61))
        self.label_4.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_username = QtWidgets.QLabel(Dialog)
        self.label_username.setGeometry(QtCore.QRect(30, 30, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_username.setFont(font)
        self.label_username.setStyleSheet("color:white;")
        self.label_username.setObjectName("label_username")
        self.label_welcome = QtWidgets.QLabel(Dialog)
        self.label_welcome.setGeometry(QtCore.QRect(320, 20, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_welcome.setFont(font)
        self.label_welcome.setStyleSheet("color:white;")
        self.label_welcome.setObjectName("label_welcome")
        self.pushButton_exit = QtWidgets.QPushButton(Dialog)
        self.pushButton_exit.setGeometry(QtCore.QRect(900, 20, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setStyleSheet("color: rgba(255, 255, 255, 210);\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"border-radius: 5px;")
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(50, 150, 671, 621))
        self.label_5.setStyleSheet("border: 0.5px solid blue;\n"
"border-radius:5px;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(760, 150, 311, 281))
        self.label_6.setStyleSheet("border: 0.5px solid blue;\n"
"border-radius:5px;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.pushButton_buy = QtWidgets.QPushButton(Dialog)
        self.pushButton_buy.setGeometry(QtCore.QRect(820, 470, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_buy.setFont(font)
        self.pushButton_buy.setStyleSheet("QPushButton#pushButton_buy {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#pushButton_buy:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#pushButton_buy:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(105, 118, 132, 200);\n"
"}")
        self.pushButton_buy.setObjectName("pushButton_buy")
        self.pushButton_info = QtWidgets.QPushButton(Dialog)
        self.pushButton_info.setGeometry(QtCore.QRect(820, 550, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_info.setFont(font)
        self.pushButton_info.setStyleSheet("QPushButton#pushButton_info {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#pushButton_info:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#pushButton_info:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(105, 118, 132, 200);\n"
"}")
        self.pushButton_info.setObjectName("pushButton_info")
        self.pushButton_history = QtWidgets.QPushButton(Dialog)
        self.pushButton_history.setGeometry(QtCore.QRect(820, 630, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_history.setFont(font)
        self.pushButton_history.setStyleSheet("QPushButton#pushButton_history {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#pushButton_history:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#pushButton_history:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(105, 118, 132, 200);\n"
"}")
        self.pushButton_history.setObjectName("pushButton_history")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(50, 110, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(760, 110, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 160, 651, 601))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(770, 160, 291, 261))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.movieListWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.movieListWidget)  # Add QListWidget to the layout

        self.sheduleListWidget = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.verticalLayout_2.addWidget(self.sheduleListWidget)

        self.pushButton_buy.clicked.connect(self.buy_ticket)
        self.pushButton_exit.clicked.connect(self.back_to_login)
        self.pushButton_history.clicked.connect(self.history)
        self.pushButton_info.clicked.connect(self.movie_info)

        
        try:
            response = requests.get("https://aiatulla.pythonanywhere.com/listmovies")
            if response.status_code == 200:
                movie_titles = response.text.split("<br>")
                for movie in movie_titles:
                    self.movieListWidget.addItem(movie)
                self.movieListWidget.itemClicked.connect(self.display_schedule)
        except Exception as e:
            print(f"Error fetching movie list: {e}")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Movie Ticket Booking"))

    def display_schedule(self, item):
        movie_title = item.text()
        print(f"Fetching schedules for movie: {movie_title}")

        try:
            response = requests.get(f"https://aiatulla.pythonanywhere.com/viewschedules?title={movie_title}")
            if response.status_code == 200:
                self.selected_movie = movie_title  # Store selected movie
                self.sheduleListWidget.clear()  # Clear previous schedules
                schedules = response.text.split("<br>")
                for schedule in schedules:
                    self.sheduleListWidget.addItem(schedule)
                self.sheduleListWidget.itemClicked.connect(self.select_schedule)
                self.seats_quantity = len(schedule)
            else:
                self.sheduleListWidget.clear()
                self.sheduleListWidget.addItem(f"No schedules found for '{movie_title}'.")
        except Exception as e:
            print(f"Error fetching schedules for '{movie_title}': {e}")
            self.sheduleListWidget.clear()
            self.sheduleListWidget.addItem(f"Error fetching schedules for '{movie_title}'.")

    def select_schedule(self, item):
        self.selected_schedule = item.text()
        print(f"Selected schedule: {self.selected_schedule}")

    def buy_ticket(self):
        if not self.selected_movie or not self.selected_schedule:
            QtWidgets.QMessageBox.warning(None, "Selection Error", "Please select a movie and schedule.")
            return

        from Seats import CinemaBooking
        self.cinema_booking_window = CinemaBooking(self.username,self.password,self.selected_movie, self.selected_schedule)
        self.cinema_booking_window.exec_()

    def movie_info(self):
        if self.selected_movie:
            from cinema_movie_info import Ui_Movie_info
            self.menu.close()
            info_window = QDialog()
            ui = Ui_Movie_info(self.selected_movie,self.selected_schedule,self.seats_quantity,self.username,self.password)
            ui.setupUi(info_window)
            info_window.exec()

        

    def history(self):
        from history import Ui_history
        self.menu.close()
        history_window = QDialog()
        ui = Ui_history(self.username,self.password)
        ui.setupUi(history_window)
        history_window.exec()


    def back_to_login(self):
        from login_cinema import Ui_Login
        self.menu.close()
        login_window = QDialog()
        ui = Ui_Login()  
        ui.setupUi(login_window)
        login_window.exec()

        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_username.setText(_translate("Dialog", self.username))
        self.label_welcome.setText(_translate("Dialog", "W e l c o m e    t o     M O V E A I T"))
        self.pushButton_exit.setText(_translate("Dialog", "B a c k"))
        self.pushButton_buy.setText(_translate("Dialog", "B u y"))
        self.pushButton_info.setText(_translate("Dialog", "M o v i e   I n f o"))
        self.pushButton_history.setText(_translate("Dialog", "H i s t o r y"))
        self.label_7.setText(_translate("Dialog", "Films:"))
        self.label_8.setText(_translate("Dialog", "Shedule:"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_menu(username="a",password='a')
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
