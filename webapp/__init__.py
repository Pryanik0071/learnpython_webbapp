from flask import Flask, render_template, request, jsonify

from webapp.model import db
from webapp.model import Book, Publisher, Category, book_category
from webapp.insert_books import insert_books_db

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    admin = Admin(app)
    admin.add_view(ModelView(Book, db.session))
    admin.add_view(ModelView(Category, db.session))

    @app.route('/')
    def index():
        return render_template('main_page.html')

    @app.route('/books/')
    def books():
        # TODO: Warning:(19, 59) Unresolved attribute reference 'desc' for class 'int'
        years_list = db.session.query(Book.year).group_by(Book.year).order_by(Book.year.desc())
        publisher_list = Publisher.query.all()
        query = db.session.query(Book).order_by(Book.year.desc())
        skill = request.args.get('skill')
        language = request.args.get('language')
        publisher = request.args.get('publisher')
        theme = request.args.get('theme')
        year = request.args.get('year')

        if skill:
            query = query.filter(Book.categories.any(name=skill))
        if language:
            query = query.filter(Book.categories.any(name=language))
        if theme:
            query = query.filter(Book.categories.any(name=theme))
        if publisher:
            query = query.join(Publisher).filter(Publisher.title == publisher)
        if year:
            query = query.filter(Book.year == year)

        book_list = query.all()

        return render_template('books.html', book_list=book_list,
                               years_list=years_list, publishers=publisher_list)

    @app.route('/book/<int:id_book>/')
    def book_info(id_book):
        book_data = Book.query.get(id_book)
        if book_data:
            return render_template('book_details.html',
                                   book_data=book_data)
        # TODO: Заглушка
        return 'Error!'

    @app.route('/get-books/', methods=['POST'])
    def get_books():
        data = request.get_json()
        authorization_header = request.headers.get('Authorization')
        if authorization_header == app.config['AUTHORIZATION_TOKEN']:
            insert_books_db(data)
            return jsonify(data)
        return jsonify({'detail': 'authentication failed'})

    return app
