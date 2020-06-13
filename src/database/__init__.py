from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

db = SQLAlchemy()

# TODO - get from env vars
SQLALCHEMY_DATABASE_URI = 'postgresql://nick@localhost:5432/casting_agency_dev'


def setup_db(app):
    print("setup_db: setting up app: ", app)
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    # db.create_all()
    # migrate = Migrate(app, db)
