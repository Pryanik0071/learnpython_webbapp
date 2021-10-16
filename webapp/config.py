import os

config_dir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = ('sqlite:///' +
                           os.path.join(config_dir, '..', 'webapp.db'))
