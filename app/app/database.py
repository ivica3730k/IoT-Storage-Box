import datetime
import json
import uuid

from flask_sqlalchemy import SQLAlchemy

import settings

db = SQLAlchemy(settings.app)


class ApiKey(db.Model):
    __tablename__ = 'apikey'
    id = db.Column(db.String(36), unique=True, nullable=False, primary_key=True, default=str(uuid.uuid4()))
    data = db.relationship('Data', backref='apikey', lazy='dynamic', cascade="all, delete-orphan")

    def __str__(self):
        return self.id


class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(36), db.ForeignKey('apikey.id'))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    data = db.Column(db.Text())

    def collection_json(self):
        """

        :return:
        """
        _data = {}
        _data = json.loads(self.data)
        _data["timestamp"] = str(self.timestamp)
        _data = json.dumps(_data)
        return "\"" + str(self.id) + "\":" + _data

    def standalone_json(self):
        """

        :return:
        """
        return self.data


def _create_api_key(api_key: str) -> ApiKey:
    """

    :param api_key:
    :return:
    """
    key = ApiKey()
    key.id = api_key
    db.session.add(key)
    db.session.commit()
    return key


def _api_key_exist(api_key: str) -> bool:
    """

    :param api_key:
    :return:
    """
    try:
        val = ApiKey.query.filter_by(id=api_key)[0]
        return True
    except IndexError:
        return False


def _get_api_key(api_key: str) -> ApiKey:
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
    if _api_key_exist(api_key):
        key = _get_api_key(api_key)
        db.session.delete(key)
        db.session.commit()


def remove_api_key_single(api_key: str, id_to_delete: int) -> None:
    """

    :param api_key:
    :param id_to_delete:
    :return:
    """
    if _api_key_exist(api_key):
        key = _get_api_key(api_key)
        key = str(key)
        try:
            result = Data.query.filter_by(key=key, id=id_to_delete).one()
            db.session.delete(result)
            db.session.commit()
        except:
            pass


def write_data(api_key: str, data) -> None:
    """

    :param api_key:
    :param data:
    :return:
    """
    if _api_key_exist(api_key):
        key = _get_api_key(api_key)
    else:
        key = _create_api_key(api_key)
    newDataObject = Data()
    newDataObject.key = key
    newDataObject.data = data
    key.data.append(newDataObject)
    db.session.add(key)
    db.session.add(newDataObject)
    db.session.commit()


def obtain_all_data(api_key: str) -> str:
    """

    :param api_key:
    :return:
    """
    out = "{"
    if _api_key_exist(api_key):
        key = _get_api_key(api_key)
        data = []
        for i in key.data.all():
            data.append(i.collection_json())
        out += ",".join(data)
    out += "}"
    return out


db.create_all()
db.session.commit()
