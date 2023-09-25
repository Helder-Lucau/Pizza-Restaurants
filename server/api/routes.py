from flask import make_response, request, jsonify
from flask_restful import Resource
from . import api
from api.models import db, Restaurant, Pizza, RestaurantPizza

class Index(Resource):

    def get(self):

        response_dict = {
            "message": "Welcome to Pizzaria",
        }
        response = make_response(
            jsonify(response_dict),
            200
        )
        return response

api.add_resource(Index, '/')

class Restaurants(Resource):
    def get(self):

        restaurant_dict = [r.to_dict() for r in Restaurant.query.all()]
        response = make_response(jsonify(restaurant_dict), 200)
        return response

api.add_resource(Restaurants, '/restaurants')

class RestaurantByID(Resource):

    def get(self, id):

        restaurant_by_id = Restaurant.query.filter_by(id=id).first()
        if restaurant_by_id:
            response = make_response(jsonify(restaurant_by_id), 200)
        else:
            response_body = {"error": "Restaurant not found"}
            response = make_response(response_body, 404)
        return response
    
    def delete(self, id):

        restaurant_by_id = Restaurant.query.filter_by(id=id).first()
        if restaurant_by_id:
            db.session.delete(restaurant_by_id)
            db.session.commit()
            response_body = {"message": "restaurant deleted successfully"}
            response = make_response(response_body, 200)
        else:
            response_body = {"error": "Restaurant does not exist"}
            response = make_response(response_body, 404)
        return response
    
api.add_resource(RestaurantByID, '/restaurants/<int:id>')

class Pizzas(Resource):

    def get(self):

        response_dict = [p.to_dict() for p in Pizza.query.all()]

        response = make_response(
            jsonify(response_dict), 
            200
        )
        return response
    
api.add_resource(Pizzas, '/pizzas')
    
class RestaurantPizzas(Resource):
    def post(self):
        new_restaurant_pizza = RestaurantPizza(
            price=request.get_json['price'],
            pizza_id=request.get_json['pizza_id'],
            restaurant_id=request.get_json['restaurant_id']
        )
        db.session.add(new_restaurant_pizza)
        db.session.commit()

        response_dict = new_restaurant_pizza.to_dict()
        response = make_response(jsonify(response_dict), 201)
        return response
    
api.add_resource(RestaurantPizzas, '/restaurant_pizzas')

