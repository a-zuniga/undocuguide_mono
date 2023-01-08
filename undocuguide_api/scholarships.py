from flask import Blueprint, request, jsonify
from models import Scholarship
from db_operations import *

scholarships = Blueprint('scholarships', __name__)

@scholarships.route('/scholarships', methods=['GET'])
def list_scholarships():
    """Endpoint to list all scholarships in the database.

    Returns:
        json: A list of dictionaries representing the scholarships.
    """
    scholarship_list = []
    for scholarship in scholarship_collection.find():
        # Convert the ObjectId fields to strings
        scholarship['_id'] = str(scholarship['_id'])
        scholarship_list.append(scholarship)
    return jsonify(scholarship_list)


@scholarships.route('/scholarships', methods=['POST'])
def create_scholarship():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No input data provided'}), 400

    # Validate the input data using the schema
    # errors = scholarship_schema.validate(data)
    # if errors:
    #     return jsonify(errors), 400

    try:
        new_scholarship = Scholarship(name=data['name'], description=data['description'], amount=data['amount'], deadline=data['deadline'], url=data['url'])
        create_scholarship_in_db(new_scholarship)
        return jsonify({'message': 'Scholarship created successfully'})
    except Exception as e:
        print(data)
        return jsonify({'message': 'Error creating scholarship', 'error': str(e)}), 500
    

@scholarships.route('/scholarships/<scholarship_id>', methods=['GET'])
def read_scholarship(scholarship_id):
    scholarship = read_scholarship_from_db(scholarship_id)
    if scholarship:
        return jsonify(scholarship)
    else:
        return jsonify({'message': 'Scholarship not found'})
        

@scholarships.route('/scholarships/<scholarship_id>', methods=['PUT'])
def update_scholarship(scholarship_id):
    scholarship = read_scholarship_from_db(scholarship_id)
    if scholarship:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'No input data provided'}), 400
        
        # Validate the input data using the schema
        # errors = scholarship_schema.validate(data)
        # if errors:
        #     return jsonify(errors), 400

        updated_scholarship = Scholarship(name=data['name'], description=data['description'], amount=data['amount'], deadline=data['deadline'], url=data['url'])
        update_scholarship_in_db(scholarship_id, updated_scholarship)
        return jsonify({'message': 'Scholarship updated successfully'})
    else:
        return jsonify({'message': 'Scholarship not found'})

@scholarships.route('/scholarships/<scholarship_id>', methods=['DELETE'])
def delete_scholarship(scholarship_id):
    scholarship = read_scholarship_from_db(scholarship_id)
    if scholarship:
        delete_scholarship_from_db(scholarship_id)
        return jsonify({'message': 'Scholarship deleted successfully'})
    else:
        return jsonify({'message': 'Scholarship not found'})
