from sqlalchemy.orm import validates

from . import db


class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)
    image_link = db.Column(db.String(500), nullable=True)
    website = db.Column(db.String(120), nullable=True)

    def short(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
        }

    def long(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'image_link': self.image_link,
            'website': self.website,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    def __repr__(self):
        return f'<Movie {self.id} {self.title}>'


class Actor(db.Model):
    __tablename__ = 'actors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Enum('M', 'F', name="gender"), nullable=False)
    phone = db.Column(db.String(120), nullable=True)
    image_link = db.Column(db.String(500), nullable=True)
    website = db.Column(db.String(120), nullable=True)

    @validates('age')
    def validate_age(self, key, age):
        if type(age) is str:
            try:
                age = int(age)
            except Exception as e:
                print('error casting the age to an int ', e)
                raise AssertionError('The age value could not be cast into an integer')

        if age < 0:
            raise AssertionError('Age should an integer > 0')

        return age

    def short(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
        }

    def long(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'phone': self.phone,
            'image_link': self.image_link,
            'website': self.website,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    def __repr__(self):
        return f'<Actor {self.id} {self.name}>'


# TODO - create model for actors_for_movie
