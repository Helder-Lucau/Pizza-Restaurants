from flask import make_response, request, jsonify
from flask_restful import Resource
from . import api
from api.models import db, Restaurant, Pizza, RestaurantPizza

class Restaurant(Resource):
    def get(self):

        restaurant_dict = [restaurant.to_dict() for restaurant in Restaurant.query.all()]
        response = make_response(jsonify(restaurant_dict),200)
        return response

api.add_resource(Restaurant, '/restaurants')

class RestaurantByID(Resource):

    def get(self, id):

        restaurant_dict = Restaurant.query.filter_by(id=id).first().to_dict()
        response = make_response(jsonify(restaurant_dict), 200)
        return response
    
    def delete(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        db.session.delete(restaurant)
        db.session.commit()

        restaurant_dict = {"message": "record successfully deleted"}

        response = make_response(jsonify(restaurant_dict),200)
        return response
    
api.add_resource(RestaurantByID, '/restaurants/<int:id>')

class Pizza(Resource):
    def get(self):
        pizza_dict = [pizza.to_dict() for pizza in Pizza.query.all()]
        response = make_response(jsonify(pizza_dict), 200)
        return response
    
    def post(self, id):
        