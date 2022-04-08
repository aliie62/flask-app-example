# -*- coding: utf-8 -*-

from flask_restful import Api
from resources.item import ItemResource, ItemListResource
from resources.user import UserResource, UserRegister, UserLogin, TokenReferesh
from resources.store import StoreListResource,StoreResource

#Define app end points
def get_endpoints(app):
    api = Api(app)
    api.add_resource(UserResource,'/user/<int:user_id>')
    api.add_resource(UserLogin,'/login')
    api.add_resource(TokenReferesh, '/refresh')
    api.add_resource(ItemListResource,'/items')
    api.add_resource(ItemResource,'/item','/item/<string:name>')
    api.add_resource(UserRegister,'/register')
    api.add_resource(StoreResource, '/store','/store/<string:name>')
    api.add_resource(StoreListResource,'/stores')
    return api
