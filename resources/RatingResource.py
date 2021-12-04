from flask_restful import reqparse, Resource
from flask import make_response   # returns an HTML response
from services.RatingService import *
import json

post_parser = reqparse.RequestParser()
post_parser.add_argument('value', type=str)
post_parser.add_argument('profile', type=str)

headers = {'Content-Type': 'application/json'}

class RatingResource(Resource):
    def get(self, investor_id=None, startup_id=None, rating_id=None):
        if startup_id is None and investor_id is not None:
            response = get_rating_by_Inv(investor_id, rating_id)
            return make_response(response.to_json(), 200, headers)
        if investor_id is None and startup_id is not None:
            response = get_rating_by_str(startup_id, rating_id)
            return make_response(response.to_json(), 200, headers)
        if investor_id is None and startup_id is None:
            response= get_rating(rating_id)
            return make_response(response.to_json(), 200, headers)

    def delete(self,investor_id=None,rating_id=None):
        if investor_id is not None and rating_id is not None:
            response = delete_rating_by_inv(investor_id,rating_id)
            return make_response(response.to_json(), 200, headers)
        return 400

    def post(self,investor_id=None, startup_id=None):
       if startup_id==None:
           args = post_parser.parse_args()
           response = create_rating_by_inv(investor_id,args.value, args.profile)
           return make_response(response.to_json(), 200, headers)
       if investor_id==None:
           args = post_parser.parse_args()
           response = create_rating_by_str(startup_id,args.value, args.profile)
           return make_response(response.to_json(), 200, headers)


