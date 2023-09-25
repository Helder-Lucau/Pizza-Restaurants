from random import randint, choice as rc
from faker import Faker
from faker_food import FoodProvider

from app import app
from api.models import db, Pizza, Restaurant, RestaurantPizza 


fake = Faker()
fake.add_provider(FoodProvider)
with app.app_context():

    Pizza.query.delete()
    Restaurant.query.delete()
    RestaurantPizza.query.delete()

    pizzas = []
    for i in range(20):
        pizza = Pizza(
            name = fake.dish(),
            ingredients = fake.ingredient()
        )
        pizzas.append(pizza)
    db.session.add_all(pizzas)
    db.session.commit()

    restaurants = []
    for i in range(30):
        add_restaurant = Restaurant(
            name=fake.city(),
            address=fake.address(),
        )
        restaurants.append(add_restaurant)
    db.session.add_all(restaurants)
    db.session.commit()