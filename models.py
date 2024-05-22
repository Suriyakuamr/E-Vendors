#original
'''
from flask_login import UserMixin
from datetime import datetime
 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  
 
 

class User(UserMixin, db.Model):
    __tablename__ = 'user'     
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False) 
    phone_number = db.Column(db.String(10),nullable=False, unique=True)    
    purchase_history = db.relationship('PurchaseHistory', back_populates='user')
    delivery_addresses = db.relationship('DeliveryAddress', backref='user', lazy=True)
     
     
     
    purchase_history_items = db.relationship('PurchaseHistory', back_populates='user', lazy=True)  
    
    def get_id(self):
        return str(self.id)

# models.py
class DeliveryAddress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    door_no = db.Column(db.String(50), nullable=False)
    street_name = db.Column(db.String(255), nullable=False)
    area = db.Column(db.String(255), nullable=False)
    landmark = db.Column(db.String(255), nullable=True)
    pincode = db.Column(db.String(10), nullable=False)
    district = db.Column(db.String(255), nullable=False)
    mobile_number = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    #created_at = db.Column(Date, default=datetime.utcnow.date)
     

    def __repr__(self):
        return f"DeliveryAddress(id={self.id}, user_id={self.user_id}, door_no={self.door_no}, street_name={self.street_name}, area={self.area}, " \
               f"landmark={self.landmark}, pincode={self.pincode}, district={self.district}, mobile_number={self.mobile_number}, created_at={self.created_at})"
 
     
     
     

 
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(255), nullable=True) 
    specifications = db.Column(db.String(255), nullable=True)
    features = db.Column(db.String(255), nullable=True)
    warranty = db.Column(db.String(255), nullable=True)
    purchase_history = db.relationship('PurchaseHistory', back_populates='product')
    def __repr__(self):
        return f"<Product {self.name}>"
    #purchase_history_items = db.relationship('PurchaseHistory', back_populates='product', lazy=True)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    product_name = db.Column(db.String(255), nullable=False)
    product_image = db.Column(db.String(255), nullable=False)
    product_price = db.Column(db.Float, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    #created_at = db.Column(Date, default=datetime.utcnow.date)
     

    def __repr__(self):
        return f"Cart(id={self.id}, user_id={self.user_id}, product_id={self.product_id}, quantity={self.quantity}, " \
               f"product_name={self.product_name}, product_image={self.product_image}, product_price={self.product_price}, " \
               f"total_price={self.total_price}, created_at={self.created_at})"
     

    user = db.relationship('User', backref=db.backref('cart_items', lazy=True))
    product = db.relationship('Product', backref=db.backref('cart_items', lazy=True))
    purchase_history_id = db.Column(db.Integer, db.ForeignKey('purchase_history.id'), nullable=True)
    purchase_history = db.relationship('PurchaseHistory', back_populates='cart')
 
     


class PurchaseHistory(db.Model):
    __tablename__ = 'purchase_history'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  
    purchase_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    #purchase_date = db.Column(db.Date,nullable=False, default=datetime.utcnow.date)    
       
    
    product_name = db.Column(db.String(255), nullable=False)
    product_image = db.Column(db.String(255), nullable=True)
    quantity = db.Column(db.Integer, nullable=False)
    product_price = db.Column(db.Float, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    #cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=True)  

    user = db.relationship('User', back_populates='purchase_history')
    product = db.relationship('Product', back_populates='purchase_history')
    cart = db.relationship('Cart', back_populates='purchase_history')   
 
    

from app import app
db.init_app(app)    '''



from flask_login import UserMixin
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(10), nullable=False, unique=True)
    purchase_history = db.relationship('PurchaseHistory', back_populates='user', lazy=True)
    delivery_addresses = db.relationship('DeliveryAddress', backref='user', lazy=True)
    cart_items = db.relationship('Cart', backref='user', lazy=True)  # Added this to simplify access to cart items

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, email={self.email})"

class DeliveryAddress(db.Model):
    __tablename__ = 'delivery_address'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    door_no = db.Column(db.String(50), nullable=False)
    street_name = db.Column(db.String(255), nullable=False)
    area = db.Column(db.String(255), nullable=False)
    landmark = db.Column(db.String(255), nullable=True)
    pincode = db.Column(db.String(10), nullable=False)
    district = db.Column(db.String(255), nullable=False)
    mobile_number = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"DeliveryAddress(id={self.id}, user_id={self.user_id}, door_no={self.door_no}, street_name={self.street_name}, area={self.area}, landmark={self.landmark}, pincode={self.pincode}, district={self.district}, mobile_number={self.mobile_number}, created_at={self.created_at})"

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(255), nullable=True)
    specifications = db.Column(db.String(255), nullable=True)
    features = db.Column(db.String(255), nullable=True)
    warranty = db.Column(db.String(255), nullable=True)
    purchase_history = db.relationship('PurchaseHistory', back_populates='product', lazy=True)
    cart_items = db.relationship('Cart', backref='product', lazy=True)  # Added this to simplify access to cart items

    def __repr__(self):
        return f"<Product {self.name}>"

class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    product_name = db.Column(db.String(255), nullable=False)
    product_image = db.Column(db.String(255), nullable=False)
    product_price = db.Column(db.Float, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    purchase_history_id = db.Column(db.Integer, db.ForeignKey('purchase_history.id'), nullable=True)

    def __repr__(self):
        return f"Cart(id={self.id}, user_id={self.user_id}, product_id={self.product_id}, quantity={self.quantity}, product_name={self.product_name}, product_image={self.product_image}, product_price={self.product_price}, total_price={self.total_price}, created_at={self.created_at})"

    purchase_history = db.relationship('PurchaseHistory', back_populates='cart')

class PurchaseHistory(db.Model):
    __tablename__ = 'purchase_history'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    purchase_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    product_name = db.Column(db.String(255), nullable=False)
    product_image = db.Column(db.String(255), nullable=True)
    quantity = db.Column(db.Integer, nullable=False)
    product_price = db.Column(db.Float, nullable=False)
    total_price = db.Column(db.Float, nullable=False)

    user = db.relationship('User', back_populates='purchase_history')
    product = db.relationship('Product', back_populates='purchase_history')
    cart = db.relationship('Cart', back_populates='purchase_history', lazy=True)

    def __repr__(self):
        return f"PurchaseHistory(id={self.id}, product_id={self.product_id}, user_id={self.user_id}, purchase_date={self.purchase_date}, product_name={self.product_name}, quantity={self.quantity}, product_price={self.product_price}, total_price={self.total_price})"

from app import app
db.init_app(app)



 