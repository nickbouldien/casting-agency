from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

# TODO - get from env vars
SQLALCHEMY_DATABASE_URI = 'postgresql://nick@localhost:5432/casting_agency_dev'


'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app):
    print("setup_db: setting up app: ", app)
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    # db.create_all()
    migrate = Migrate(app, db)


'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
'''


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
