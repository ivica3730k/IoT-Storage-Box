import settings
from flask import request
import json
import database as db

app = settings.app


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/<apikey>/put/')
def put(apikey: str):
    db.write_data(apikey, json.dumps(dict(request.args)))
    return apikey


app.run(debug=True, use_reloader=True)
