from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import uuid
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class ApiKey(db.Model):
    __tablename__ = 'apikey'
    id = db.Column(db.String(36), unique=True, nullable=False, primary_key=True, default=str(uuid.uuid4()))
    data = db.relationship('Data', backref='apikey', lazy='dynamic', cascade="all, delete-orphan")


class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(36), db.ForeignKey('apikey.id'))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    data = db.Column(db.Text())