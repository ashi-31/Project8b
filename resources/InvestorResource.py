from flask_restful import reqparse, Resource
from flask import make_response   # returns an HTML response
from services.InvestorService import *
from flask_jwt_extended import jwt_required, get_jwt_identity
import json

post_parser = reqparse.RequestParser()
post_parser.add_argument('first_name', type=str)
post_parser.add_argument('last_name', type=str)
post_parser.add_argument('email', type=str)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('email', type=str)

headers = {'Content-Type': 'application/json'}


class InvestorResource(Resource):
    @jwt_required()
    def get(self, investor_id=None):
        if investor_id is None:
            args = reqparse.request.args
            #query_fil = str(args.get('field'))
            query_sort = str(args.get('sortby'))
            #query_dir = str(args['sortdir'])
            query_from = int(args['from']) if 'from' in args else 0
            query_count = int(args['count']) if 'count' in args else 1000
            investor = get_investor_count(query_sort, query_from, query_count)
        else:
            investor = get_investor(investor_id)
        return make_response(investor.to_json(), 200, headers)

    @jwt_required()
    def delete(self, investor_id=None):
        if investor_id is not None:
            response = delete_investor(investor_id)
            return make_response(response.to_json(), 200, headers)
        return 400

    @jwt_required()
    def post(self):
        args = post_parser.parse_args()
        response = create_investor(args.first_name,args.last_name, args.email)
        return make_response(response.to_json(), 200, headers)

    @jwt_required()
    def patch(self, investor_id=None):
        if investor_id is not None:
            args = patch_parser.parse_args()
            response = update_investor(investor_id, args.email)
            return make_response(response.to_json(), 200, headers)
        return 400