#!/usr/bin/python3
'''
Create Flask app; app_views
'''
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def api_status():
    """
    status route
    :return: response with json
    """
    response = {'status': "OK"}

    resp = jsonify(data)
    resp.status_code = 200

    return resp


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """
    stats of all objs route
    :return: json of all objs
    """
    stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User'),
    }

    resp = jsonify(data)
    resp.status_code = 200

    return resp
