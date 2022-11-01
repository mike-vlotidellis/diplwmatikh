from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader 
def load_user(user_id):
    return User.query.get(int(user_id)) #tha epistrepsei ta stoixia tou user me id to (user_id) 

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
   
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Product(db.Model):
    barcode = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)
    name = db.Column(db.String(20) ,nullable=False)
    kind = db.Column(db.String(20))
    quantity = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(20), nullable=False, default='default.jpg')
    warehouse_id = db.Column(db.String(20), nullable =False )

    def __repr__(self):
        return f"Product('{self.barcode}', '{self.name}', '{self.kind}', '{self.quantity}', '{self.image}', '{self.warehouse_id}')"

class Warehouse(db.Model):
    house_id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)
    address = db.Column(db.String(20), nullable=False, unique=True)
    house_name = db.Column(db.String(30) ,nullable=False, unique=True)

    def __repr__(self):
        return f"Warehouse('{self.house_id}', '{self.address}', '{self.house_name}')"