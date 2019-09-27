# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:52:38 2019

@author: hosseal
"""

from flask_restful import Resource,reqparse
from flask_jwt_extended import jwt_required
from models.item import Item


class ItemResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True)
    parser.add_argument('price',type=float,required=True)

    parser_name = reqparse.RequestParser()
    parser_name.add_argument('name', type=str, required=True)

    @jwt_required
    def get(self, name):
        item = Item.find_by_name(name)
        return item.json() , 200 if item else 404

    @jwt_required
    def post(self):
        try:
            params = ItemResource.parser.parse_args()
            item = Item(**params)
        except:
            return {'message':'The passed data is not in expected format.'}, 400
        else:
            try:
                existing_item = Item.find_by_name(item.name)
                if existing_item:
                    return {'message':f'Item with name <{existing_item.name}> already exists.'}, 400
                else:
                    item.save_to_db()
                    return {'message':'Item was added successfully.'}, 200
            except:
                return {'message':'An error occurred in inserting the item.'}, 500

    @jwt_required
    def put(self):
        try:
            params = ItemResource.parser.parse_args()
            new_item = Item(**params)
        except:
            return {'message':'The passed data is not in expected format.'}, 400
        else:
            try:
                item = Item.find_by_name(new_item.name)
                if item:
                    item.price = new_item.price
                else:
                    item = new_item
                item.save_to_db()
                return {'message':'Item was added/updated successfully.'}, 201
            except:
                return {'message':'An error occurred in updating the item.'}, 500

    @jwt_required
    def delete(self):
        try:
            params = ItemResource.parser_name.parse_args()
            item = Item.find_by_name(params['name'])
        except:
            return {'message':'The passed data is not in expected format.'}, 400
        else:
            try:
                item.delete_from_db()
                return {'message':'Item was deleted successfully.'}, 200
            except:
                return {'message':'An error occurred in deleting data.'}, 500

class ItemListResource(Resource):
    @jwt_required
    def get(self):
        try:
            items = Item.find_all()
            items_dic = [item.json() for item in items]
            return {'items':items_dic}, 200
        except:
            return {'message':'An error occurred reading data.'}, 500
