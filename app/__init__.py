"""Module that contains the route for the obtaining the shortest path."""

from flask import request, jsonify
from flask_api import FlaskAPI

def create_app():
    app = FlaskAPI(__name__, instance_relative_config=True)
    @app.route('/apiv1/shortestpath/', methods=['POST', 'GET'])
    def shortestpath():
        response = jsonify({
            'path': {
                "0":"b6",
                "1":"d7",
                "2":"c5",
                "3":"d3",
                "4":"e1"},
            'status': 'success'
        })
        response.status_code = 200
        return response
    return app
