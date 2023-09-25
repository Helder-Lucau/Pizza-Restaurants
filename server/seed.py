from random import randint, choice as rc
from faker import Faker

from app import app
from api.models import db, Pizza, Restaurant, RestaurantPizza 

restaurant_list = [
    "Urban Burger",
    "Pizza Inn",
    "Urban Grill",
    "Lion King",
    "Java House",
    "Big Square",
    "Pizza Hut",
    "Dominion Pizza"
]

fake = Faker()
with app.app_context():

    Pizza.query.delete()
    Restaurant.query.delete()
    RestaurantPizza.query.delete()

    pizzas = []
    for i in range(20):
        pizza = Pizza(
            name = fake.name(),
            ingredients = fake.text()
        )
        pizzas.append(pizza)
    db.session.add_all(pizzas)
    db.session.commit()

    restaurants = []
    for i in range(20):
        add_restaurant = Restaurant(
            name=restaurant_list,
            address=fake.address(),
        )
        restaurants.append(add_restaurant)
    db.session.add_all(restaurants)
    db.session.commit()