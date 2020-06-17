import os

DATABASE_URL = os.environ.get('DATABASE_URL', None)

environment = os.environ.get('FLASK_ENV', 'production')
print("*** environment *** => ", environment)

if DATABASE_URL is None:
    raise Exception("the database url cannot be empty. check the `DATABASE_URL` environment variable: ", DATABASE_URL)

SQLALCHEMY_DATABASE_URI = DATABASE_URL
print("SQLALCHEMY_DATABASE_URI: ", SQLALCHEMY_DATABASE_URI)

SQLALCHEMY_TRACK_MODIFICATIONS = False
