from datetime import datetime

from flask_login import UserMixin

from finder import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    """Return a User instance with that user_id."""
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """Map the user table (with an ORM)

    Contain user information fields needed by the system (i.e. auth).
    Link to the profile table with a 1-to-1 relationship.
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    profile = db.relationship('Profile', backref='parent', uselist=False)

    def __repr__(self):
        return f'Username: {self.username}, Email: {self.email}\n'


class Profile(db.Model):
    """Map the profile table (with an ORM)

    Contain profile information fields needed by other users (i.e. contact search).
    Link to the user table with a user_id Foreign Key field.
    """
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(60))
    nick_name = db.Column(db.String(60))
    email = db.Column(db.String(60))
    phone_number = db.Column(db.String(30))
    address = db.Column(db.String(60))
    profile_pic = db.Column(db.String(60))
    birth_date = db.Column(db.DateTime)
    birth_place = db.Column(db.String(60))
    website = db.Column(db.String(60))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)

    def __repr__(self):
        return f'Full Name: {self.full_name}, Phone: {self.phone_number}\n'
