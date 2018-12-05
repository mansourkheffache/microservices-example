from inventory import api
from flask_restful import Resource, reqparse
from inventory.models import Order, Delivery
from inventory.helper import CustomJSONEncoder, pretty
from pymodm.connection import connect
from bson import json_util, ObjectId
from flask import jsonify
import datetime
import json
import sys


# # Connect to MongoDB and call the connection "my-app".
connect("mongodb://localhost:27017/dev")

parser = reqparse.RequestParser()
parser.add_argument('address')
parser.add_argument('bill', type=float)
parser.add_argument('name')
parser.add_argument('items', action='append')
parser.add_argument('_id')

class OrderEntity(Resource):
	# View order by ID
	def get(self, order_id):
		order = Order.objects.get({'_id': ObjectId(order_id)})
		order.to_son()
		return jsonify(pretty(order))

	# Delete order by ID


api.add_resource(OrderEntity, '/orders/<order_id>')

class OrderList(Resource):
	# Create a new order
	def post(self):
		args 	= parser.parse_args()
		name 	= args['name']
		items 	= args['items']
		bill 	= args['bill']
		destination = args['address']
		creation_date = datetime.datetime.now()

		# TODO: add id and delivery at saving Order

		order = Order( name=name, bill=bill, items=items, creation_date=creation_date, destination=destination)
		order.save()
		return jsonify(pretty(order))

	# Get list of orders
	# Filter by user name (optional)
	def get(self):
		args = parser.parse_args()
		orders = Order.objects.all()
		name = None
		try:
			print('\n\n\nIn name filter')
			name = args['name']
			orders = Order.objects.get_queryset().raw({'name': name})
			return jsonify(pretty(orders))
		except:
			pass

		return jsonify(pretty(orders))

api.add_resource(OrderList, '/orders')

# class OrderListOneUser(Resource):
# 	# Get list of orders for a single user
# 	def get(self, name):
# 		args = parser.parse_args()
# 		# orders = Order.objects.all()
# 		orders = Order.objects.get( {'name' : name })
# 		return jsonify(pretty(orders))