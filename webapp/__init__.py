from flask import Flask, render_template, request, jsonify

from webapp.model import db
from webapp.model import Book, Author
from webapp.insert_books import insert_books_db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        return render_template('base.html')

    @app.route('/books')
    def books():
        book_list = Book.query.all()
        # authors = book_list.book_author
        # print(authors)
        # print(book_list)
        return render_template('book.html', book_list=book_list)

    @app.route('/get-books/', methods=['POST'])
    def get_books():
        data = request.get_json()
        authorization_header = request.headers.get('Authorization')
        if authorization_header == app.config['AUTHORIZATION_TOKEN']:
            insert_books_db(data)
            return jsonify(data)
        return jsonify({'detail': 'authentication failed'})

    return app
