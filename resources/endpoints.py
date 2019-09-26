# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:58:30 2019

@author: hosseal
"""

from flask_restful import Api
from resources.item import ItemResource, ItemListResource
from resources.user import UserResource, UserRegister
from resources.store import StoreListResource,StoreResource


def get_endpoints(app):
    api = Api(app)
    #item endpoints
    api.add_resource(ItemListResource,'/items')
    api.add_resource(ItemResource,'/item','/item/<string:name>')
    api.add_resource(UserRegister,'/register')
    api.add_resource(UserResource,'/user/<string:user_id>')
    api.add_resource(StoreResource, '/store','/store/<string:name>')
    api.add_resource(StoreListResource,'/stores')
    return api
