
from PyQt5 import QtCore, QtGui, QtWidgets
import requests


class Ui_Movie_info(object):
    def __init__(self,movie,schedule,seats_quantity,username,password):
        self.movie = movie
        self.schedule = schedule
        self.seats_quantity = seats_quantity
        self.booked_s = 0
        self.seats = str((self.seats_quantity-1)*30)
        self.username = username
        self.password = password
        

    def setupUi(self, Dialog):
        self.info = Dialog
        Dialog.setObjectName("Movie info")
        Dialog.resize(620, 730)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 601, 711))
        self.label.setStyleSheet("background-image: url(images/UserMenu_back.jpeg);\n"
"border-radius:5px;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 350, 561, 361))
        self.label_2.setStyleSheet("background-color:white;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 360, 541, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_filfm_title = QtWidgets.QLabel(Dialog)
        self.label_filfm_title.setGeometry(QtCore.QRect(30, 20, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_filfm_title.setFont(font)
        self.label_filfm_title.setStyleSheet("color:white;")
        self.label_filfm_title.setObjectName("label_filfm_title")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 310, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:white;")
        self.label_6.setObjectName("label_6")
        self.pushButton_back = QtWidgets.QPushButton(Dialog)
        self.pushButton_back.setGeometry(QtCore.QRect(430, 20, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setStyleSheet("color: rgba(255, 255, 255, 210);\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"border-radius: 5px;")
        self.pushButton_back.setObjectName("pushButton_back")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 80, 561, 221))
        self.label_4.setStyleSheet("background-color:white;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(60, 130, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color:rgba(52, 204, 235,0.9);\n"
"color: rgba(255, 255, 255, 210);\n"
"border-radius:5px;\n"
"\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(60, 200, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color:rgba(52, 204, 235,0.9);\n"
"color: rgba(255, 255, 255, 210);\n"
"border-radius:5px;\n"
"\n"
"")
        self.label_8.setObjectName("label_8")
        self.label_film_time = QtWidgets.QLabel(Dialog)
        self.label_film_time.setGeometry(QtCore.QRect(240, 20, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_film_time.setFont(font)
        self.label_film_time.setStyleSheet("color:white;")
        self.label_film_time.setObjectName("label_film_time")
        self.label_all_quantity = QtWidgets.QLabel(Dialog)
        self.label_all_quantity.setGeometry(QtCore.QRect(230, 130, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_all_quantity.setFont(font)
        self.label_all_quantity.setStyleSheet("background-color:rgba(52, 204, 235,0.9);\n"
"color: rgba(255, 255, 255, 210);\n"
"border-radius:5px;\n"
"\n"
"")
        self.label_all_quantity.setObjectName("label_all_quantity")
        self.label_all_seats = QtWidgets.QLabel(Dialog)
        self.label_all_seats.setGeometry(QtCore.QRect(230, 200, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_all_seats.setFont(font)
        self.label_all_seats.setStyleSheet("background-color:rgba(52, 204, 235,0.9);\n"
"color: rgba(255, 255, 255, 210);\n"
"border-radius:5px;\n"
"\n"
"")
        self.label_all_seats.setObjectName("label_all_seats")
        self.label_sold_quantity = QtWidgets.QLabel(Dialog)
        self.label_sold_quantity.setGeometry(QtCore.QRect(410, 130, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_sold_quantity.setFont(font)
        self.label_sold_quantity.setStyleSheet("background-color:rgba(52, 204, 235,0.9);\n"
"color: rgba(255, 255, 255, 210);\n"
"border-radius:5px;\n"
"\n"
"")
        self.label_sold_quantity.setObjectName("label_sold_quantity")
        self.label_booked_seats = QtWidgets.QLabel(Dialog)
        self.label_booked_seats.setGeometry(QtCore.QRect(410, 200, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_booked_seats.setFont(font)
        self.label_booked_seats.setStyleSheet("background-color:rgba(52, 204, 235,0.9);\n"
"color: rgba(255, 255, 255, 210);\n"
"border-radius:5px;\n"
"\n"
"")
        self.label_booked_seats.setObjectName("label_booked_seats")
        self.pushButton_back.clicked.connect(self.back_to_menu)

        self.movieListWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.movieListWidget)  # Add QListWidget to the layout

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        try:
            # Correct API endpoint
            response = requests.get(f"https://aiatulla.pythonanywhere.com/viewbookingsbymovie?title={self.movie}")
            
            if response.status_code == 200:
                # Parse the JSON response
                movie_bookings = response.json().get("bookings", [])
                
                if movie_bookings:
                    for booking in movie_bookings:
                        self.movieListWidget.addItem(booking)
                        self.booked_s = +1
                else:
                    self.movieListWidget.addItem(f"No bookings found for '{self.movie}'.")
            elif response.status_code == 404:
                self.movieListWidget.addItem(f"Movie '{self.movie}' not found.")
            else:
                self.movieListWidget.addItem(f"Error fetching bookings: {response.status_code}")
        except Exception as e:
            self.movieListWidget.addItem(f"Error: {e}")
    
    
    def back_to_menu(self):
        from cinema_menu2 import Ui_menu
        self.info.close()
        menu_window = QtWidgets.QDialog()
        ui = Ui_menu(self.username,self.password)  
        ui.setupUi(menu_window)
        menu_window.exec()



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_filfm_title.setText(_translate("Dialog", self.movie))
        self.label_6.setText(_translate("Dialog", "People:"))
        self.pushButton_back.setText(_translate("Dialog", "B a c k"))
        self.label_5.setText(_translate("Dialog", "Quantity:"))
        self.label_8.setText(_translate("Dialog", "Seats:"))
        self.label_film_time.setText(_translate("Dialog", self.schedule))
        self.label_all_quantity.setText(_translate("Dialog", self.seats))
        self.label_all_seats.setText(_translate("Dialog", "30"))
        self.label_sold_quantity.setText(_translate("Dialog", "Quantity:"))
        self.label_booked_seats.setText(_translate("Dialog", str(self.booked_s)))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Movie_info()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
