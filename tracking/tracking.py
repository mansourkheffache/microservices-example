from flask_restful import Resource
from tracking import api
from flask import jsonify, request
from datetime import datetime
from bson import json_util, ObjectId
import json


from inventory.helper import pretty
from inventory.models import Item


class TrackingList(Resource):
	pass

class TrackingE (Resource):
	pass


api.add_resource(TrackingList, '/trackings')
api.add_resource(TrackingE, '/trackings/<item_id>')