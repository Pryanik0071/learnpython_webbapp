from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


book_author = db.Table('book_author',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True)
)


book_category = db.Table('book_category',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    authors = db.relationship('Author', secondary=book_author, lazy='subquery',
                              backref=db.backref('books', lazy='joined'))
    year = db.Column(db.SmallInteger, nullable=False)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'),
                             nullable=False)
    price = db.Column(db.Integer)
    description = db.Column(db.String)
    categories = db.relationship('Category', secondary=book_category, lazy='subquery',
                                 backref=db.backref('books', lazy='joined'))
    image = db.Column(db.String, unique=True, nullable=False)
    isbn = db.Column(db.Text, nullable=False, unique=True)

    def __repr__(self):
        return f'Book: {self.title} - id: {self.id}'


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False, unique=True)

    def __repr__(self):
        return f'Author: {self.name} id: {self.id}'


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    def __repr__(self):
        return f'Category: {self.name} - id: {self.id}'


class Publisher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    books = db.relationship('Book', backref='publisher', lazy=True)

    def __repr__(self):
        return f'Publisher: {self.title} id: {self.id}'
