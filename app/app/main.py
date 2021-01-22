import json
import os
import uuid

import jsbeautifier
from flask import render_template, request, Response

import database as db
import settings
import validators as v

app = settings.app


@app.route('/')
def hello_world():
    data = {}
    data["domain"] = settings.DOMAIN
    data["uuid4example"] = str(uuid.uuid4())
    return render_template('index.html', data=data)


@app.route('/<apikey>/put/')
def put(apikey: str):
    if v.is_valid_uuid4(apikey):
        if request.args:
            db.write_data(apikey, json.dumps(dict(request.args)))
        return "OK"
    else:
        return "INVALID API KEY, MUST BE UUID4"


@app.route('/<apikey>/get/')
def get_all(apikey: str):
    if v.is_valid_uuid4(apikey):
        return Response(jsbeautifier.beautify(db.obtain_all_data(apikey)), mimetype="application/json")
    else:
        return "INVALID API KEY, MUST BE UUID4"


@app.route('/<apikey>/remove/')
def remove(apikey: str):
    if v.is_valid_uuid4(apikey):
        db.remove_api_key(apikey)
        return "OK"
    else:
        return "INVALID API KEY, MUST BE UUID4"


@app.route('/<apikey>/remove/<id_to_delete>')
def remove_single(apikey: str, id_to_delete: int):
    if v.is_valid_uuid4(apikey):
        db.remove_api_key_single(apikey,id_to_delete)
        return "OK"
    else:
        return "INVALID API KEY, MUST BE UUID4"


def is_docker():
    path = '/proc/self/cgroup'
    return (
            os.path.exists('/.dockerenv') or
            os.path.isfile(path) and any('docker' in line for line in open(path))
    )


if __name__ == "__main__":
    if is_docker():
        app.run(host='0.0.0.0', debug=False, port=80)
    else:
        app.run(host='0.0.0.0', debug=True, port=8080)
