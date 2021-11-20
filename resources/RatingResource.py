from flask_restful import reqparse, Resource
from flask import make_response   # returns an HTML response
from services.RatingService import *
import json

post_parser = reqparse.RequestParser()
post_parser.add_argument('value', type=str)
post_parser.add_argument('profile', type=str)

headers = {'Content-Type': 'application/json'}

class RatingResource(Resource):
    def get(self, investor_id=None):
        response = get_rating_by_Inv(investor_id)
        return make_response(response.to_json(), 200, headers)

    def delete(self,investor_id=None,rating_id=None):
        if investor_id is not None and rating_id is not None:
            response = delete_rating_by_inv(investor_id,rating_id)
            return make_response(response.to_json(), 200, headers)
        return 400

    def post(self,investor_id):
        rating = get_rating_by_Inv(investor_id)
        args = post_parser.parse_args()
        response = create_rating_by_inv(investor_id,args.value,args.profile)
        return make_response(response.to_json(), 200, headers)


