from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    # author_id = db.Column(db.Integer, db.ForeignKey('category.id'),
    #                       index=True, nullable=False)
    year = db.Column(db.SmallInteger, nullable=False)
    # publisher_id = db.Column(db.Integer, db.ForeignKey('category.id'),
    #                          nullable=False)
    price = db.Column(db.Numeric(10, 2))
    description = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
                            nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    text = db.Column(db.Text, nullable=True)

    categories = db.relationship("BookCategory")

    def __repr__(self):
        return f'Book: {self.title} - id: {self.id}'


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    books = db.relationship("BookCategory")

    def __repr__(self):
        return f'Category: {self.name} - id: {self.id}'


class BookCategory(db.Model):
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), index=True, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    book = db.relationship("Book", lazy='joined')
    category = db.relationship("Category", lazy='joined')

    def __repr__(self):
        return f"Book.id: {self.book_id} Category.id: {self.category_id}"
