import os
import sqlite3
import feedparser

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from extra import login_required

# Config app
app = Flask(__name__)

# Auto reload templates
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Config session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Config db
db = SQL("sqlite:///project.db")


@app.after_request
def after_request(response):
    # Ensure responses remain uncached
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
@login_required
def index():

    # Call function that parses feeds
    entries = get_feeds()

    # and render them onto the page
    return render_template("index.html", entries=entries)

@app.route("/manage", methods=["GET", "POST"])
@login_required
def manage():
      if request.method == "POST":

           # Receive form data
           title = request.form.get("title")
           url = request.form.get("url")

           # Handle invalid feeds
           feed = feedparser.parse(url)
           if feed.bozo == 1:
               flash("Invalid Feed!")
               return redirect("/manage")

           # Insert valid feeds into database
           db.execute("INSERT INTO feeds (user_id, title, url) VALUES (?, ?, ?);",
                      session["user_id"], title, url)

           # Flash success, and redirect to manage feeds
           flash("Feed Added!")
           return redirect("/manage")

      # User reached route via GET, so list currently added feeds and render the page
      else:
        entries = db.execute("SELECT title FROM feeds WHERE user_id = ?", session["user_id"])
        return render_template("manage.html", entries=entries)

@app.route("/remove", methods=["POST"])
@login_required
def remove():
      if request.method == "POST":

        # Receive form data
        feed = request.form.get("remove-title")

        # Query if feed exists in database
        rows = db.execute("SELECT title FROM feeds WHERE title = ?", request.form.get("remove-title"))
        if len(rows) != 1:
            flash("Feed does not exist!")
            return redirect("/manage")

        # Delete feed if it is available
        db.execute("DELETE FROM feeds WHERE title = ?", feed)
        flash("Feed Deleted!")

      return redirect("/manage")

def get_feeds():

    # Store entry data in dict
    entries = []
    # Connect to database and pull feed info to be parsed
    with sqlite3.connect("project.db") as conn:
        cursor = conn.execute("SELECT title, url FROM feeds WHERE user_id = ?", (session["user_id"],))
        feed_data = cursor.fetchall()
        # For every feed fetched, parse the url
        for title, url in feed_data:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                entry_data = {
                     "title": entry.title,
                     "link": entry.link,
                     "summary": entry.summary,
                     "author": title,
                     }
                # then append the data to the dict
                entries.append(entry_data)

    return entries

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        # Receive form data
        username = request.form.get("username")
        password = request.form.get("password")

        # Query if username provided is unique
        if len(db.execute("SELECT username FROM users WHERE username = ?", username)):
            flash("Username is taken!")
            return redirect("/register")

        # Ensure password is of specified length
        if not len(password) >= 8:
            flash("Password must be more than 8 characters!")
            return redirect("/register")

        # If no errors, then input new user into database, and store password in hash for security
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?);",
                   username, generate_password_hash(password))

        # Remember user registering, and redirect them to home
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        session["user_id"] = rows[0]["id"]

        flash("Registered!")
        return redirect("/")

    # User reached route via GET, so render the page.
    else:
        return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        # Define rows
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Query if password matches stored hash
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            flash("Invalid Username and/or Password!")
            return redirect("/login")

        # Remember user logging in, and redirect them to home
        session["user_id"] = rows[0]["id"]

        return redirect("/")

    # User reached route via GET, so display the login page
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    # Clear user session and display the login page
    session.clear()

    return redirect("/")
