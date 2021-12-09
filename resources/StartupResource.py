from flask_restful import reqparse, Resource
from flask import make_response   # returns an HTML response
from services.StartupService import *
from flask_jwt_extended import jwt_required, get_jwt_identity
import json

post_parser = reqparse.RequestParser()
post_parser.add_argument('ein', type=str)
post_parser.add_argument('name', type=str)
post_parser.add_argument('email', type=str)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('email', type=str)

headers = {'Content-Type': 'application/json'}


class StartupResource(Resource):
    @jwt_required()
    def get(self, startup_id=None):
        response = get_startup(startup_id)
        return make_response(response.to_json(), 200, headers)

    @jwt_required()
    def delete(self, startup_id=None):
        if startup_id is not None:
            response = delete_startup(startup_id)
            return make_response(response.to_json(), 200, headers)
        return 400

    @jwt_required()
    def post(self):
        args = post_parser.parse_args()
        response = create_startup(args.ein,args.name, args.email)
        return make_response(response.to_json(), 200, headers)

    @jwt_required()
    def patch(self, startup_id=None):
        if startup_id is not None:
            args = patch_parser.parse_args()
            response = update_startup(startup_id, args.email)
            return make_response(response.to_json(), 200, headers)
        return 400
