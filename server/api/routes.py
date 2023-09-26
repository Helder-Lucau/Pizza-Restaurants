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

        restaurant = Restaurant.query.filter_by(id=id).first()
        if not restaurant:
            response_body = {"error": "Restaurant not found"}
            response = make_response(
                jsonify(response_body), 
                404
            )
            return response
        else:
            response_dict = restaurant.to_dict()
            response = make_response(
                jsonify(response_dict), 
                200
            )
            return response
    
    def delete(self, id):

        restaurant_by_id = Restaurant.query.filter_by(id=id).first()
        if not restaurant_by_id:
            response_body = {"error": "Restaurant does not exist"}
            response = make_response(
                jsonify(response_body), 
                404
            )
            return response
        else:
            db.session.delete(restaurant_by_id)
            db.session.commit()
            response_body = {"message": "restaurant deleted successfully"}
            response = make_response(
                jsonify(response_body),
                200
                )            
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
        user_data = request.get_json()
        new_restaurant_pizza = RestaurantPizza(
            price=user_data['price'],
            pizza_id=user_data['pizza_id'],
            restaurant_id=user_data['restaurant_id']
        )
        db.session.add(new_restaurant_pizza)
        db.session.commit()

        # if not RestaurantPizza.query.filter(RestaurantPizza.id == new_restaurant_pizza.id).first():
        #     response_body

        response_dict = new_restaurant_pizza.to_dict()
        response = make_response(jsonify(response_dict), 201)
        return response
# add the resource to the API
api.add_resource(RestaurantPizzas, '/restaurant_pizzas')

