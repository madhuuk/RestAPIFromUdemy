from flask_restful import Resource, reqparse
from models.store import StoreModel
from flask_jwt import jwt_required

items = []


class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('store_id', type=int, required=True, help="Every item needs a store ID")

    @jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'store not exist'}, 404

    @jwt_required()
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message": "The Item with Name {} already exists".format(name)}, 404

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item'}, 500

        return store.json(), 201

    @jwt_required()
    def delete(self, name):
        item = StoreModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"message": "The Item with Name {} is deleted from records".format(name)}, 201
        else:
            return {"message": "Item Not Found"}


class StoreList(Resource):
    @jwt_required()
    def get(self):
        # Using Lambda Function
        # return {'items': list(map(lambda x: x.json(),ItemModel.query.all()))}
        # OR
        # Using List comprehensions
        return {'Stores': [store.json() for store in StoreModel.query.all()]}