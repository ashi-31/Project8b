from flask_restful import reqparse, Resource
from flask import make_response   # returns an HTML response
from services.EventService import *
import json

post_parser = reqparse.RequestParser()
post_parser.add_argument('name', type=str)
post_parser.add_argument('host_name', type=str)
post_parser.add_argument('date', type=str)

headers = {'Content-Type': 'application/json'}

class EventResource(Resource):
    def get(self, investor_id=None,startup_id=None, event_id=None):
        if investor_id is not None and event_id is None and startup_id is None:
            args = reqparse.request.args
            query_sort = str(args.get('sortby'))
            # query_dir = str(args['sortdir'])
            query_from = int(args['from']) if 'from' in args else 0
            query_count = int(args['count']) if 'count' in args else 1000
            event = get_event_count_inv(investor_id,query_sort, query_from, query_count)
        elif investor_id is not None and event_id is not None and startup_id is None:
            event = get_event_by_Inv(investor_id,event_id)
        elif startup_id is not None and event_id is None and investor_id is None:
            args = reqparse.request.args
            query_sort = str(args.get('sortby'))
            # query_dir = str(args['sortdir'])
            query_from = int(args['from']) if 'from' in args else 0
            query_count = int(args['count']) if 'count' in args else 1000
            event = get_event_count_str(startup_id,query_sort, query_from, query_count)
        elif startup_id is not None and event_id is not None and investor_id is None:
            event = get_event_by_str(startup_id,event_id)
        elif startup_id is None and investor_id is None:
            event= get_event(event_id)
        return make_response(event.to_json(), 200, headers)

    def delete(self, investor_id=None, event_id=None):
        if investor_id is not None and event_id is not None:
            response = delete_event_by_inv(investor_id, event_id)
            return make_response(response.to_json(), 200, headers)
        return 400

    def post(self,investor_id=None, startup_id=None):
       if startup_id==None and investor_id is not None:
           args = post_parser.parse_args()
           response = create_event_by_inv(investor_id, args.name, args.host_name, args.date)
           return make_response(response.to_json(), 200, headers)
       if investor_id==None and startup_id is not None:
           args = post_parser.parse_args()
           response = create_event_by_str(startup_id,args.name, args.host_name, args.date)
           return make_response(response.to_json(), 200, headers)
       if investor_id is None and startup_id is None:
           args = post_parser.parse_args()
           response = create_event(args.name, args.host_name, args.date)
           return make_response(response.to_json(), 200, headers)

