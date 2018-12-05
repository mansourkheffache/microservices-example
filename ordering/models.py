from pymongo.write_concern import WriteConcern
from bson import ObjectId
from pymodm import MongoModel, fields

class Order(MongoModel):
	_id 			= fields.ObjectIdField(primary_key=True, default=ObjectId)
	name 			= fields.CharField()
	items 			= fields.ListField(field = fields.CharField())
	bill 			= fields.FloatField()
	creation_date 	= fields.DateTimeField()
	destination		= fields.CharField()
	delivery_id 	= fields.CharField()

class Delivery(MongoModel):
	_id 			= fields.ObjectIdField(primary_key=True, default=ObjectId)
	creation_date 	= fields.DateTimeField()
	delivery_date 	= fields.DateTimeField()
	status			= fields.CharField()
	current_location= fields.CharField()
	destination		= fields.CharField()
	order_id		= fields.CharField()