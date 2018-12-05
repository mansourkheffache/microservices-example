from flask import Flask, session
from flask_restful import Resource, Api
from inventory.helper import CustomJSONEncoder

app = Flask(__name__)
api = Api(app)

app.secret_key = 'SOSECRET!!!'

app.json_encoder = CustomJSONEncoder

import inventory.inventory
import inventory.ordering