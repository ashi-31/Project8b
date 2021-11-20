from flask_restful import reqparse, Resource
from flask import make_response   # returns an HTML response
from services.BankService import *
import json

post_parser = reqparse.RequestParser()
post_parser.add_argument('num', type=str)
post_parser.add_argument('name', type=str)
post_parser.add_argument('r_num', type=str)
post_parser.add_argument('check_save', type=str)
post_parser.add_argument('zip', type=str)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('name', type=str, default=False)

headers = {'Content-Type': 'application/json'}

class BankResource(Resource):
    def get(self, investor_id=None, bank_id=None):
       response = get_bank_by_Inv(investor_id, bank_id)
       return make_response(response.to_json(), 200, headers)

    def delete(self,investor_id=None,bank_id=None):
        if investor_id is not None and bank_id is not None:
            response = delete_bank_by_inv(investor_id,bank_id)
            return make_response(response.to_json(), 200, headers)
        return 400

    def post(self,investor_id):
        bank = get_bank_by_Inv(investor_id)
        args = post_parser.parse_args()
        response = create_bank_by_inv(investor_id,args.num,args.name, args.r_num, args.check_save, args.zip)
        return make_response(response.to_json(), 200, headers)

    def patch(self, investor_id=None, bank_id=None):
        if investor_id is not None and bank_id is not None:
             args = patch_parser.parse_args()
             response = patch_bank_by_Inv(investor_id,bank_id,args.name)
        return make_response(response.to_json(), 200, headers)
        return 400
