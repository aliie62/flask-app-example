# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:52:38 2019

@author: hosseal
"""

from flask_restful import Resource,reqparse
from flask_jwt_extended import jwt_required
from models.store import Store
from models.item import Item

class StoreResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True)

    @jwt_required
    def get(self, name):
        store = Store.find_by_name(name)
        return store.json() , 200 if Store else 404

    @jwt_required
    def post(self):
        try:
            params = StoreResource.parser.parse_args()
            store = Store(**params)
        except:
            return {'message':'The passed data is not in expected format.'}, 400
        else:
            try:
                existing_store = Store.find_by_name(store.name)
                if existing_store:
                    return {'message':f'Store with name <{existing_store.name}> already exists.'}, 400
                else:
                    store.save_to_db()
                    return {'message':'Store was added successfully.'}, 200
            except:
                return {'message':'An error occurred in inserting the Store.'}, 500

    @jwt_required
    def put(self, name):
        try:
            params = StoreResource.parser.parse_args()
        except:
            return {'message':'The passed data is not in expected format.'}, 400
        else:
            try:
                item = Item.find_by_name(params['name'])
                store = Store.find_by_name(name)
                if item and store:
                    store.items.append(item)
                    store.save_to_db()
                    return {'message':f'Item <{item.name}> was allocated to store <{name}> successfully.'}, 200
                else:
                    return {'message':f'Item <{item.name}> or/and store <{name}> were not found in our database.'}, 400
            except:
                return {'message':'An error occurred in allocating item to the store.'}, 500

    @jwt_required
    def delete(self):
        try:
            params = StoreResource.parser.parse_args()
            store = Store.find_by_name(params['name'])
        except:
            return {'message':'The passed data is not in expected format.'}, 400
        else:
            try:
                store.delete_from_db()
                return {'message':'Store was deleted successfully.'}, 200
            except:
                return {'message':'An error occurred in deleting data.'}, 500

class StoreListResource(Resource):
    @jwt_required
    def get(self):
        try:
            stores = Store.find_all()
            stores_dic = [store.json() for store in stores]
            return {'stores':stores_dic}, 200
        except:
            return {'message':'An error occurred reading data.'}, 500
