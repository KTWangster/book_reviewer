import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# Home/Login page
@app.route("/")
def index():
    # Login
    return "Project 1: TODO"

# Search page
@app.route("/search", methods=["POST"])
def search():
    """Search for a book."""

    # Search bar
    title = request.form.get("title")
    try:
        book_id = int(request.form.get("book_id"))
    except ValueError:
        return render_template("error.html", message="Invalid book title.")

    # Make sure book exists
    book = db.execute("SELECT * FROM books WHERE id = :id", {"id": book_id}).fetchone()
    if book is None:    
        return render_template("error.html", message="No such book.")
    db.commit()

# Book display page - Details of book + Ability to submit review
@app.route("/book", methods=["GET", "POST"])
# Displays book details

@app.route("logout", methods=["GET"])
# Displays logou message

# Allows users to submit reviews
def index():
    if request.method == "POST":
        review = request.form.get("review")
        reviews.append(review)
    
    return render_template("book.html", reviews=reviews)