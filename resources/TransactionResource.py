from flask_restful import reqparse, Resource
from flask import make_response   # returns an HTML response
from services.TransactionService import *
from flask_jwt_extended import jwt_required, get_jwt_identity
import json

post_parser = reqparse.RequestParser()
post_parser.add_argument('number', type=str)
post_parser.add_argument('amount', type=str)
post_parser.add_argument('date_initiated', type=str)
post_parser.add_argument('date_received', type=str)
post_parser.add_argument('investor', type=str)
post_parser.add_argument('startup', type=str)
post_parser.add_argument('status', type=str)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('status', type=str)

headers = {'Content-Type': 'application/json'}


class TransactionResource(Resource):
    @jwt_required()
    def get(self, transaction_id=None):
        if transaction_id is None:
            args = reqparse.request.args
            query_sort = str(args.get('sortby'))
            # query_dir = str(args['sortdir'])
            query_from = int(args['from']) if 'from' in args else 0
            query_count = int(args['count']) if 'count' in args else 1000
            transaction = get_transaction_count(query_sort, query_from, query_count)
        else:
            transaction = get_transaction(transaction_id)
        return make_response(transaction.to_json(), 200, headers)

    @jwt_required()
    def delete(self, transaction_id=None):
        if transaction_id is not None:
            response = delete_transaction(transaction_id)
            return make_response(response.to_json(), 200, headers)
        return 400

    @jwt_required()
    def post(self):
        args = post_parser.parse_args()
        response = create_transaction(args.number,args.amount, args.date_initiated, args.date_received, args.investor, args.startup, args.status)
        return make_response(response.to_json(), 200, headers)

    @jwt_required()
    def patch(self, transaction_id=None):
        if transaction_id is not None:
            args = patch_parser.parse_args()
            response = update_transaction(transaction_id, args.status)
            return make_response(response.to_json(), 200, headers)
        return 400