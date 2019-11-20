from myproject import db, login, app
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin


@login.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    profile_pic = db.Column(db.String(64), default='/static/pics/default.jpg', nullable=False)
    post = db.relationship('Thoughts', backref='author', lazy='dynamic')
    user_comments = db.relationship('comments', backref='user_comments', lazy='joined')

    def __init__(self, email, username, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, field):
        return check_password_hash(self.password, field)


class Thoughts(db.Model):
    __tabelname__ = 'thoughts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    text = db.Column(db.Text)
    private_or_public = db.Column(db.Boolean, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, text, message, user_id, pri):
        self.text = text
        self.text = message
        self.user_id = user_id
        self.private_or_public = pri
