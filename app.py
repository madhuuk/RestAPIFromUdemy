import os

from flask import Flask
from flask_restful import Api
from security import authenticate, identity
from resources.item import Item, ItemList
from resources.store import Store, StoreList

from flask_jwt import JWT
from resources.user import userregister

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' 
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.secret_key = 'MADHU'
api = Api(app)

jwt = JWT(app, authenticate, identity)
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(userregister, '/register')

if __name__ == "__main__":
    app.run(debug=True)
