from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Pizza(db.Model, SerializerMixin):
     __tablename__ = 'pizzas'

     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String)
     ingredients = db.Column(db.String)
     created_at = db.Column(db.DateTime, server_default=db.func.now())
     updated_at = db.Column(db.DateTime, onupdate=db.func.now())

     def __repr__(self):
        return f'Name={self.name} Ingredients={self.ingredients}'

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    address = db.Column(db.String)

    def __repr__(self):
        return f'Name={self.name} Address={self.address}'

class RestaurantPizza(db.Model, SerializerMixin):
     __tablename__ = 'restaurant_pizzas'

     id = db.Column(db.Integer, primary_key=True)
     pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
     restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
     price = db.Column(db.Float)

     created_at = db.Column(db.DateTime, server_default=db.func.now())
     updated_at = db.Column(db.DateTime, onupdate=db.func.now())

     def __repr__(self):
        return f'Price={self.price} pizza={self.pizza_id} restaurant={self.restaurant_id}'