from flask import Flask , request, render_template, jsonify

app=Flask(__name__)

class Cinema:
    def __init__(self):
        self.admins=[('Ayatulla','1234')]
        self.movies = []
        self.users = {}

    def get_user(self,name,password):
        if name in self.users and password == self.users[name]:
            return True

    def add_movie(self, movie):
        if movie not in self.movies:
            self.movies.append(movie)


    def add_user(self,name,password):
        self.users[name] = password


    def list_movies(self):
        return [movie.title for movie in self.movies]

    def remove_movie(self, title):
        for movie in self.movies:
            if movie.title == title:
                self.movies.remove(movie)
                print(f"Movie '{title}' has been removed.")
                return
        print(f"Movie '{title}' not found.")

    def cinema_earning(self):
        total_earning = sum(movie.movie_earning() for movie in self.movies)
        print(f"Total Cinema Earnings: ${total_earning:.2f}")
        return total_earning


class Movie:
    def __init__(self, title, price):
        self.title = title
        self.schedules = []
        self.price = price
        self.seats = {}

    def add_schedule(self, schedule):
        if schedule in self.schedules:
            print(f"Schedule '{schedule}' already exists for {self.title}.")
            return
        self.schedules.append(schedule)
        self.seats[schedule] = {
            chr(ord('A') + j) + str(i + 1): None for i in range(6) for j in range(5)
        }
        print(f"Schedule '{schedule}' added for {self.title}.")

    def remove_schedule(self, schedule):
        if schedule in self.schedules:
            self.schedules.remove(schedule)
            del self.seats[schedule]
            print(f"Schedule '{schedule}' has been removed from {self.title}.")
        else:
            print(f"Schedule '{schedule}' not found for {self.title}.")

    def book_seat(self, client, schedule, seat):
        if schedule not in self.schedules:
            print(f"Schedule '{schedule}' does not exist.")
            return
        if seat not in self.seats[schedule]:
            print(f"Seat '{seat}' does not exist.")
            return
        if self.seats[schedule][seat]:
            print(f"Seat '{seat}' is already booked.")
            return

        self.seats[schedule][seat] = str(client.username+client.password)
        client.add_booking(self.title, schedule, seat)
        print(f"Seat '{seat}' successfully booked for {client.username} in '{self.title}' at {schedule}.")

    def get_seats(self, schedule):
        if schedule not in self.schedules:
            print(f"Schedule '{schedule}' does not exist.")
            return {}
        return self.seats[schedule]

    def list_schedules(self):
        return self.schedules

    def movie_schedule_earning(self, schedule):
        if schedule not in self.schedules:
            print(f"Schedule '{schedule}' does not exist for {self.title}.")
            return 0.0
        booked_seats = sum(1 for seat in self.seats[schedule].values() if seat)
        earning = booked_seats * self.price
        print(f"Earnings for '{self.title}' at '{schedule}': ${earning:.2f}")
        return earning

    def movie_earning(self):
        total_earning = sum(self.movie_schedule_earning(schedule) for schedule in self.schedules)
        print(f"Total Earnings for '{self.title}': ${total_earning:.2f}")
        return total_earning


class Client:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.booking_history = []

    def add_booking(self, title, schedule, seat):
        self.booking_history.append(f"{title} --> {schedule} --> {seat}")

    def view_booking_history(self):
        return self.booking_history

    def remove_booking(self, title, schedule, seat):
        booking = f"{title} --> {schedule} --> {seat}"
        if booking in self.booking_history:
            self.booking_history.remove(booking)
            print(f"Booking '{booking}' has been removed for {self.username}.")
        else:
            print(f"Booking '{booking}' not found for {self.username}.")



cinema=Cinema()
clients={}
@app.route('/addmovie')
def add_movie():
    title = request.args.get('title')
    price = request.args.get('price')
    if title and price:
        cinema.add_movie(Movie(title, float(price)))
        return f"Movie '{title}' added successfully with a price of ${price}."
    return "Error: Provide valid 'title' and 'price'."

@app.route('/listmovies')
def list_movies():
    return "<br>".join(cinema.list_movies()) if cinema.movies else "No movies available."

@app.route('/removemovie')
def remove_movie():
    title = request.args.get('title')
    if title:
        cinema.remove_movie(title)
        return f"Movie '{title}' removed successfully."
    return "Error: Provide a valid 'title'."

@app.route('/earnings')
def cinema_earnings():
    total = cinema.cinema_earning()
    return f"Total cinema earnings: ${total:.2f}"

@app.route('/addclient')
def add_client():
    username = request.args.get('username')
    password = request.args.get('password')
    if username and password:
        if username in clients:
            return f"Error: Client '{username}' already exists."
        clients[username] = Client(username, password)
        return f"Client '{username}' added successfully."
    return "Error: Provide both 'username' and 'password'."

@app.route('/viewclients')
def view_clients():
    return "<br>".join(clients.keys()) if clients else "No clients registered."

@app.route('/bookseat')
def book_seat():
    username = request.args.get('username')
    password = request.args.get('password')
    title = request.args.get('title')
    schedule = request.args.get('schedule')
    seat = request.args.get('seat')
    client = clients.get(username)

    if client and client.password == password:
        for movie in cinema.movies:
            if movie.title == title:
                movie.book_seat(client, schedule, seat)
                return f"Seat '{seat}' booked for '{username}' in '{title}' at '{schedule}'."
        return f"Error: Movie '{title}' not found."
    return "Error: Invalid username or password."

@app.route('/viewbookings')
def view_bookings():
    username = request.args.get('username')
    password = request.args.get('password')
    client = clients.get(username)

    if client and client.password == password:
        return "<br>".join(client.view_booking_history()) if client.booking_history else "No bookings found."
    return "Error: Invalid username or password."

@app.route('/addschedule')
def add_schedule():
    title = request.args.get('title')
    schedule = request.args.get('schedule')
    for movie in cinema.movies:
        if movie.title == title:
            movie.add_schedule(schedule)
            return f"Schedule '{schedule}' added to '{title}'."
    return f"Error: Movie '{title}' not found."

@app.route('/viewschedules')
def view_schedules():
    title = request.args.get('title')
    for movie in cinema.movies:
        if movie.title == title:
            schedules = movie.list_schedules()
            return "<br>".join(schedules) if schedules else f"No schedules available for '{title}'."
    return f"Error: Movie '{title}' not found."

@app.route('/viewseats')
def view_seats():
    title = request.args.get('title')
    schedule = request.args.get('schedule')
    for movie in cinema.movies:
        if movie.title == title:
            seats = movie.get_seats(schedule)
            if seats:
                return "<br>".join([f"{seat}: {'Booked' if booked else 'Available'}" 
                                    for seat, booked in seats.items()])
            return f"Error: Schedule '{schedule}' not found for '{title}'."
    return f"Error: Movie '{title}' not found."

if __name__ == '__main__':
    app.run(debug=True)