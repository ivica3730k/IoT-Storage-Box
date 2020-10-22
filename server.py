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


def create_api_key(api_key: str) -> ApiKey:
    """

    :param api_key:
    :return:
    """
    key = ApiKey()
    key.id = api_key
    db.session.add(key)
    db.session.commit()
    return key


def api_key_exist(api_key: str) -> bool:
    """

    :param api_key:
    :return:
    """
    try:
        val = ApiKey.query.filter_by(id=api_key)[0]
        return True
    except IndexError:
        return False


def get_api_key(api_key: str) -> ApiKey:
    """

    :param api_key:
    :return:
    """
    try:
        return ApiKey.query.filter_by(id=api_key)[0]
    except IndexError as e:
        raise ValueError("API Key not present in database") from e


def remove_api_key(api_key: str) -> None:
    """

    :param api_key:
    :return:
    """
    key = get_api_key(api_key)
    db.session.delete(key)
    db.session.commit()


def write_data(api_key: str, data) -> None:
    """

    :param api_key:
    :param data:
    :return:
    """
    if api_key_exist(api_key):
        key = get_api_key(api_key)
    else:
        key = create_api_key(api_key)
    newDataObject = Data()
    newDataObject.key = key
    newDataObject.data = data
    key.data.append(newDataObject)
    db.session.add(key)
    db.session.add(newDataObject)
    db.session.commit()
