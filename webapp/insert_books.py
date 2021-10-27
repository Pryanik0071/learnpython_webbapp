from webapp.model import db
from webapp.model import Category, Publisher, book_category, book_author, Author, Book


def insert_books_db(books_from_parser: dict):
    for publisher_name, publisher_value in books_from_parser.items():
        print(publisher_name)
        publisher_db = Publisher.query.filter(Publisher.title == publisher_name).first()
        if publisher_db:
            id_publisher = publisher_db.id
        else:
            new_publisher = Publisher(title=publisher_name)
            db.session.add(new_publisher)
            db.session.flush()
            id_publisher = new_publisher.id
        print(id_publisher)
        for category_name, category_value in publisher_value.items():
            print(category_name)
            category_db = Category.query.filter(Category.name == category_name).first()
            if category_db:
                id_category = category_db.id
            else:
                new_category = Category(name=category_name)
                db.session.add(new_category)
                db.session.flush()
                id_category = new_category.id
            print(id_category)
            print(category_value)
            for book_info in category_value.values():
                id_authors = []
                for author in book_info['authors']:
                    print(author)
                    author_db = Author.query.filter(Author.name == author).first()
                    if author_db:
                        id_author = author_db.id
                    else:
                        new_author = Author(name=author)
                        db.session.add(new_author)
                        db.session.flush()
                        id_author = new_author.id
                    id_authors.append(id_author)

                print(id_authors)

                book_db = Book.query.filter(Book.isbn == book_info['isbn']).first()
                if book_db:
                    # TODO: CHECK DATA + UPDATE FUNC
                    pass
                else:
                    new_book = Book(title=book_info['title'],
                                    year=book_info['year'],
                                    publisher_id=id_publisher,
                                    price=book_info['price'],
                                    description=book_info['description'],
                                    image=book_info['image'],
                                    isbn=book_info['isbn'])
                    db.session.add(new_book)
                    db.session.flush()
                    id_book = new_book.id

                    statement = book_category.insert().values(book_id=id_book, category_id=id_category)
                    db.session.execute(statement)

                    for id_author in id_authors:

                        statement = book_author.insert().values(book_id=id_book, author_id=id_author)
                        db.session.execute(statement)

    db.session.commit()
