from flask import Flask, jsonify
from faker import Faker
import random

app = Flask(__name__)

fake = Faker()

# Generate 10 random books with titles, authors, and prices
def generate_random_books(num_books=10):
    books = []
    for _ in range(num_books):
        book = {
            "title": fake.catch_phrase(),
            "author": fake.name(),
            "price": round(random.uniform(5.0, 50.0), 2)  # Generate a random price between 5.0 and 50.0
        }
        books.append(book)
    return books

# Generate 10 random books when the server starts
books = generate_random_books()

@app.route('/')
def index():
    return "Hello"

@app.route('/books', methods=['GET'])
def find_all_books():
    return jsonify(books), 200, {'Content-Type': 'application/json'}

@app.route('/books/<int:id>', methods=['GET'])
def findbyid(id):
    return f"find by id: {id}"

@app.route('/books', methods=['POST'])
def create():
    jsonstring = request.json
    return f"create book: {jsonstring}"

@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    jsonstring = request.json
    return f"update book {id}: {jsonstring}"

@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    return f"delete book {id}"

if __name__ == "__main__":
    app.run(debug=True)


