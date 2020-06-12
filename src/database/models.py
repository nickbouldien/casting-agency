from . import db


class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image_link = db.Column(db.String(500))
    website = db.Column(db.String(120), nullable=True)
    release_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Movie {self.id} {self.name}>'


class Actor(db.Model):
    __tablename__ = 'actors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(20))
    phone = db.Column(db.String(120), nullable=True)
    image_link = db.Column(db.String(500), nullable=True)
    website = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return f'<Actor {self.id} {self.name}>'

