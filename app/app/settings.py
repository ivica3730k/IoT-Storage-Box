import os
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DOMAIN = "yourdomainorurl"
try:  
    DOMAIN = os.environ["domain"]
except KeyError: 
    pass