from flask import Flask, render_template, request, jsonify

from webapp.model import db
from webapp.model import Book, Publisher, Category, book_category
from webapp.insert_books import insert_books_db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        return render_template('base.html')

    @app.route('/books/')
    def books():
        # TODO: Warning:(19, 59) Unresolved attribute reference 'desc' for class 'int'
        years_list = db.session.query(Book.year).group_by(Book.year).order_by(Book.year.desc())
        publisher_list = Publisher.query.all()
        query = db.session.query(Book).order_by(Book.year.desc())
        year = request.args.get('year')
        publisher = request.args.get('publisher')
        language = request.args.get('language')
        category = request.args.get('category')
        skill = request.args.get('skill')

        if year:
            query = query.filter(Book.year == year)
        if publisher:
            query = query.join(Publisher).filter(Publisher.title == publisher)

        book_list = query.all()

        return render_template('books.html', book_list=book_list,
                               years_list=years_list, publishers=publisher_list)

    # @app.route('/books/')
    # def books():
    #     query = db.session.query(Book)
    #     year = request.args.get('year')
    #     min_price = request.args.get('min_price')
    #
    #     if year:
    #         query = query.filter(Book.year == year)
    #
    #     if min_price:
    #         min_price = int(min_price)
    #         query = query.filter(Book.price >= min_price)
    #
    #     book_list = query.all()
    #
    #     # book_list = db.session.query(Book).join(Publisher).all()
    #     # authors = book_list.book_author
    #     # print(authors)
    #     # print(book_list)
    #     return render_template('books.html', book_list=book_list)

    @app.route('/book/<int:id_book>/')
    def book_info(id_book):
        book_data = Book.query.get(id_book)
        print(book_data)
        if book_data:
            print(book_data.id)
        return render_template('book_details.html',
                               book_data=book_data)

    @app.route('/get-books/', methods=['POST'])
    def get_books():
        data = request.get_json()
        authorization_header = request.headers.get('Authorization')
        if authorization_header == app.config['AUTHORIZATION_TOKEN']:
            insert_books_db(data)
            return jsonify(data)
        return jsonify({'detail': 'authentication failed'})

    return app
