from flask_restful import reqparse, Resource
from flask import make_response
from services.FundService import *
import json

post_parser = reqparse.RequestParser()
post_parser.add_argument('amount', type=str)
post_parser.add_argument('startup_name', type=str)
post_parser.add_argument('investor_name', type=str)

headers = {'Content-Type': 'application/json'}

class FundResource(Resource):
    def get(self, investor_id=None, fund_id=None):
        if investor_id is not None and fund_id is None:
            args = reqparse.request.args
            query_sort = str(args.get('sortby'))
            # query_dir = str(args['sortdir'])
            query_from = int(args['from']) if 'from' in args else 0
            query_count = int(args['count']) if 'count' in args else 1000
            transaction = get_fund_count(investor_id,query_sort, query_from, query_count)
        else:
            transaction = get_fund_by_Inv(fund_id)
        return make_response(transaction.to_json(), 200, headers)

    def delete(self,investor_id=None,fund_id=None):
        if investor_id is not None and fund_id is not None:
            response = delete_fund_by_inv(investor_id,fund_id)
            return make_response(response.to_json(), 200, headers)
        return 400

    def post(self,investor_id):
        fund = get_fund_by_Inv(investor_id)
        args = post_parser.parse_args()
        response = create_fund_by_inv(investor_id,args.amount,args.startup_name, args.investor_name)
        return make_response(response.to_json(), 200, headers)

