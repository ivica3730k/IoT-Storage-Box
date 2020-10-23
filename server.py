import settings
from flask import request
from flask import Response
import json
import database as db
import jsbeautifier

app = settings.app


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/<apikey>/put/')
def put(apikey: str):
    if request.args:
        db.write_data(apikey, json.dumps(dict(request.args)))
    return "OK"


@app.route('/<apikey>/get/')
def get_all(apikey: str):
    return Response(jsbeautifier.beautify(db.obtain_all_data(apikey)), mimetype="application/json")


@app.route('/<apikey>/remove/')
def remove(apikey: str):
    db.remove_api_key(apikey)
    return "OK"


app.run(debug=True, use_reloader=True)
