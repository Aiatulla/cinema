import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QDialog, QGridLayout, QPushButton, QVBoxLayout,
    QLabel, QMessageBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class CinemaBooking(QDialog):
    def __init__(self, username, password, movie, schedule):
        super().__init__()
        self.setWindowTitle("Cinema Booking")
        self.username = username
        self.password = password
        self.movie = movie
        self.schedule = schedule

        # Fetch seats for the specific movie and schedule
        self.seat_status = self.fetch_seat_status()

        self.buttons = {}
        self.init_ui()

    def fetch_seat_status(self):
        """Fetch seat status from the server."""
        try:
            response = requests.get(
                "https://aiatulla.pythonanywhere.com/viewseats",
                params={"title": self.movie, "schedule": self.schedule},
            )
            if response.status_code == 200:
                seats = response.text.split("<br>")
                seat_map = {}
                for seat_entry in seats:
                    seat_name, status = seat_entry.split(":")
                    seat_name = seat_name.strip()
                    seat_map[seat_name] = None if "Available" in status else "occupied"
                return seat_map
            else:
                QMessageBox.warning(self, "Error", f"Failed to fetch seat data: {response.status_code}")
        except requests.RequestException as e:
            QMessageBox.warning(self, "Error", f"Network error: {e}")
        return {}

    def init_ui(self):
        # Setting window size
        self.resize(900, 700)

        # Main layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # Title
        title = QLabel("Welcome to the Cinema")
        title.setFont(QFont("Georgia", 26, QFont.Bold))
        title.setStyleSheet("color: #3E4A61;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        subtitle = QLabel("Select your seats")
        subtitle.setFont(QFont("Arial", 16))
        subtitle.setStyleSheet("color: #6B7A8F;")
        subtitle.setAlignment(Qt.AlignCenter)
        layout.addWidget(subtitle)

        # Grid layout for seat buttons
        grid_layout = QGridLayout()
        grid_layout.setSpacing(20)

        # Rows and columns for seats
        rows = ["A", "B", "C", "D", "E", "F"]
        cols = [1, 2, 3, 4, 5]

        for i, row in enumerate(rows):
            for j, col in enumerate(cols):
                seat_name = f"{row}{col}"
                button = QPushButton(seat_name)
                button.setFixedSize(90, 60)
                button.setFont(QFont("Arial", 11, QFont.Bold))

                # Set seat color based on status
                status = self.seat_status.get(seat_name, None)
                self.set_seat_color(button, status)

                button.clicked.connect(lambda checked, b=button: self.toggle_seat(b))
                grid_layout.addWidget(button, i, j)
                self.buttons[seat_name] = button

        layout.addLayout(grid_layout)

        # Confirm Purchase button
        buy_button = QPushButton("Confirm Purchase")
        buy_button.setFont(QFont("Arial", 14, QFont.Bold))
        buy_button.setStyleSheet(
            "background-color: #4CAF50; color: white; padding: 10px 20px; border-radius: 10px; border: 2px solid #388E3C;"
        )
        buy_button.clicked.connect(self.confirm_booking)
        layout.addWidget(buy_button)

        # Go Back button
        back_button = QPushButton("Go Back")
        back_button.setFont(QFont("Arial", 14, QFont.Bold))
        back_button.setStyleSheet(
            "background-color: #FF5252; color: white; padding: 10px 20px; border-radius: 10px; border: 2px solid #E53935;"
        )
        back_button.clicked.connect(self.go_back)
        layout.addWidget(back_button)

        # Set main layout
        self.setLayout(layout)
        self.setStyleSheet("background-color: #F5F7FA;")

    def set_seat_color(self, button, status):
        """Set button color based on seat status."""
        if not status:
            color = "#8BC34A"  # Free (green)
        elif status == "selected":
            color = "#FFEB3B"  # Selected (yellow)
        elif status == self.username + self.password:
            color = "#2196F3"  # Booked by the current user (blue)
        else:
            color = "#E57373"  # Booked by another user (red)
        button.setStyleSheet(f"background-color: {color}; color: white; border-radius: 15px;")

    def toggle_seat(self, button):
        """Handle seat selection or deselection."""
        seat_name = button.text()
        current_status = self.seat_status.get(seat_name, None)

        if current_status is None:
            # Seat is free
            self.seat_status[seat_name] = "selected"
        elif current_status == "selected":
            # Seat is selected, deselect it
            self.seat_status[seat_name] = None
        elif current_status == self.username + self.password:
            # Seat is already booked by this user, allow deselection
            self.seat_status[seat_name] = None
        else:
            # Seat is booked by another user
            QMessageBox.warning(self, "Seat Occupied", f"Seat {seat_name} is already booked by another user.")
            return

        self.set_seat_color(button, self.seat_status[seat_name])

    def confirm_booking(self):
        """Confirm booking of selected seats."""
        selected_seats = [seat for seat, status in self.seat_status.items() if status == "selected"]

        if not selected_seats:
            QMessageBox.information(self, "No Seats Selected", "Please select at least one seat before purchasing.")
            return

        successful_bookings = []
        failed_bookings = []

        for seat_name in selected_seats:
            try:
                response = requests.get(
                    "https://aiatulla.pythonanywhere.com/bookseat",
                    params={
                        "username": self.username,
                        "password": self.password,
                        "title": self.movie,
                        "schedule": self.schedule,
                        "seat": seat_name,
                    },
                )
                if response.status_code == 200:
                    successful_bookings.append(seat_name)
                    self.seat_status[seat_name] = self.username + self.password
                    self.set_seat_color(self.buttons[seat_name], self.seat_status[seat_name])
                else:
                    failed_bookings.append(seat_name)
            except requests.RequestException as e:
                QMessageBox.warning(self, "Network Error", f"Failed to book seat {seat_name}: {e}")

        if successful_bookings:
            QMessageBox.information(
                self,
                "Booking Confirmed",
                f"Successfully booked: {', '.join(successful_bookings)}.",
            )

        if failed_bookings:
            QMessageBox.warning(
                self,
                "Booking Failed",
                f"Could not book: {', '.join(failed_bookings)}. Please try again.",
            )

    def go_back(self):
        """Go back to the previous screen."""
        self.close()



# if __name__ == "__main__":
#     # Initialize the PyQt5 application
#     app = QApplication(sys.argv)

#     # Example data: Replace with real inputs or fetch dynamically
#     username = "user1"
#     password = "pass1"
#     movie = "Inception"
#     schedule = "12:00"

#     # Create and show the CinemaBooking window
#     window = CinemaBooking(username, password, movie, schedule)
#     window.show()

#     # Execute the application
#     sys.exit(app.exec_())
