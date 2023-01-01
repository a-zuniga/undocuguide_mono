from app import app as flask_app
from models import Scholarship
from flask import request as flask_request, jsonify, Blueprint
from controllers import *

scholarships = Blueprint('scholarships', __name__)

@flask_app.route('/scholarships', methods=['POST'])
def create_scholarship():
    data = flask_request.get_json()
    if not data:
        return jsonify({'message': 'No input data provided'}), 400
    new_scholarship = Scholarship(name=data['name'], description=data['description'], amount=data['amount'], deadline=data['deadline'], url=data['url'])
    create_scholarship_in_db(new_scholarship)
    return jsonify({'message': 'Scholarship created successfully'})

@flask_app.route('/scholarships/<scholarship_id>', methods=['GET'])
def read_scholarship(scholarship_id):
    scholarship = read_scholarship_from_db(scholarship_id)
    if scholarship:
        return jsonify(scholarship)
    else:
        return jsonify({'message': 'Scholarship not found'})

@flask_app.route('/scholarships/<scholarship_id>', methods=['PUT'])
def update_scholarship(scholarship_id):
    scholarship = read_scholarship(scholarship_id)
    if scholarship:
        data = flask_request.get_json()
        if not data:
            return jsonify({'message': 'No input data provided'}), 400
        updated_scholarship = Scholarship(name=data['name'], description=data['description'], amount=data['amount'], deadline=data['deadline'], url=data['url'])
        update_scholarship_in_db(scholarship_id, updated_scholarship)
        return jsonify({'message': 'Scholarship updated successfully'})
    else:
        return jsonify({'message': 'Scholarship not found'})

@flask_app.route('/scholarships/<scholarship_id>', methods=['DELETE'])
def delete_scholarship(scholarship_id):
    scholarship = read_scholarship(scholarship_id)
    if scholarship:
        delete_scholarship_from_db(scholarship_id)
        return jsonify({'message': 'Scholarship deleted successfully'})
    else:
        return jsonify({'message': 'Scholarship not found'})
