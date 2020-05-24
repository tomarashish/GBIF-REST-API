from flask import Flask, Blueprint, Response, request, send_file
from flask import render_template, redirect, url_for, make_response
from flask_restplus import Api, Resource, reqparse
from flask_restplus import Model, fields, marshal_with
from flask import jsonify, abort
import os
import re
import sys
from io import BytesIO
import zipfile
import pandas as pd

app = Flask(__name__)

api = Api(app)
# Create a URL route in our application for "/"

'''
species_model = api.model('Model', {
    'task': 'fields.String',
    'uri': "fields.Url('todo_ep')"
})
'''


species_ns = api.namespace(
    name="species", description="Species searching by name"
)

species_parser = reqparse.RequestParser()
# species_parser.add_argument("")


@species_ns.route('/species')
class Species(Resource):
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:   varinats json
    """
    # @api.marshal_with(var_model)

    def get(self, id):

        return {'var_name': '34868', 'var_type': 'Snp'}


taxonomy_ns = api.namespace(
    name="taxonomy", description="Taxonomy searching by name"
)


@taxonomy_ns.route('/taxonomy/')
class Taxonomy(Resource):
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:   varinats json
    """
    # @api.marshal_with(var_model)

    def get(self, id):

        return {'var_name': '34868', 'var_type': 'Snp'}


observation_ns = api.namespace(
    name="observation", description="Species searching by name"
)


@observation_ns.route('/observation/<string:hgsgv_names>/list')
class Observations(Resource):
    """
    """

    def get(self, id):
        pass


if __name__ == "__main__":
    app.run(debug=True, port=5001)
