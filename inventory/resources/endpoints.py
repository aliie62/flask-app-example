# -*- coding: utf-8 -*-

from flask_restful import Api
from inventory.resources.item import ItemResource, ItemListResource
from inventory.resources.user import (
    UserResource,
    UserRegister,
    UserLogin,
    UserLogout,
    TokenReferesh,
)
from inventory.resources.store import StoreListResource, StoreResource


# Define app end points
def get_endpoints(app):
    api = Api(app)
    api.add_resource(UserResource, "/user/<int:user_id>")
    api.add_resource(UserLogin, "/login")
    api.add_resource(UserLogout, "/logout")
    api.add_resource(TokenReferesh, "/refresh")
    api.add_resource(ItemListResource, "/items")
    api.add_resource(ItemResource, "/item", "/item/<string:name>")
    api.add_resource(UserRegister, "/register")
    api.add_resource(StoreResource, "/store", "/store/<string:name>")
    api.add_resource(StoreListResource, "/stores")
    return api
