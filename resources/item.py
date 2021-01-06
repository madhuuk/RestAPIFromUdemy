from flask_restful import Resource, reqparse
from models.item import ItemModel
from flask_jwt import jwt_required

items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="This field can non be left blank")
    parser.add_argument('store_id', type=int, required=True, help="Every item needs a store ID")

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not exist'}, 404

    @jwt_required()
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message": "The Item with Name {} already exists".format(name)}, 404

        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'], data['store_id'])

        try:
            item.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item'}, 500

        return item.json(), 201

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"message": "The Item with Name {} is deleted from records".format(name)}, 201
        else:
            return {"message": "Item Not Found"}

    @jwt_required()
    def put(self, name):
        item = ItemModel.find_by_name(name)

        data = Item.parser.parse_args()

        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])  # OR ItemModel(name, **data)
        else:
            item.price = data['price']
        try:
            item.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item'}, 500

        return item.json(), 202


class ItemList(Resource):
    @jwt_required()
    def get(self):
        # Using Lambda Function
        # return {'items': list(map(lambda x: x.json(),ItemModel.query.all()))}
        # OR
        # Using List comprehensions
        return {'items': [item.json() for item in ItemModel.query.all()]}