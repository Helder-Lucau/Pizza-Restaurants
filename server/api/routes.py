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
        response = make_response(jsonify(restaurant_dict),200)
        return response

api.add_resource(Restaurants, '/restaurants')

class RestaurantByID(Resource):

    def get(self, id):

        restaurant_dict = Restaurant.query.filter_by(id=id).first().to_dict()
        response = make_response(jsonify(restaurant_dict), 200)
        return response
    
    def delete(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        
        db.session.delete(restaurant)
        db.session.commit()
        response_body = {"message": "restaurant deleted"}

        response = make_response(
            jsonify(response_body),
            200
        )
        return response
    
api.add_resource(RestaurantByID, '/restaurants/<int:id>')

class Pizzas(Resource):
    def get(self):
        pizza_dict = [n.to_dict() for n in Restaurant.query.all()]
        response = make_response(jsonify(pizza_dict),200)
        return response
    
api.add_resource(Pizzas, '/pizzas')
    
class RestaurantPizza(Resource):
    def post(self):
        new_restaurant_pizza = RestaurantPizza(
            price=request.form['price'],
            pizza_id=request.form['pizza_id'],
            restaurant_id=request.form['restaurant_id']
        )
        db.session.add(new_restaurant_pizza)
        db.session.commit()

        response_dict = new_restaurant_pizza.to_dict()
        response = make_response(jsonify(response_dict), 201)
        return response
    
api.add_resource(RestaurantPizza, '/restaurant_pizzas')

