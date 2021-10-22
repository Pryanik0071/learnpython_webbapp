from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


book_category = db.Table('book_category',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)


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
    category_id = db.relationship('Category', secondary=book_category, lazy='subquery',
                                  backref=db.backref('books', lazy=True))
    url = db.Column(db.String, unique=True, nullable=False)
    text = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'Book: {self.title} - id: {self.id}'


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'Category: {self.name} - id: {self.id}'
