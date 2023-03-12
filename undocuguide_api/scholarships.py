from flask import Blueprint, request, jsonify
from models import Scholarship
from db_operations import *
from models import scholarship_schema
import json
from jsonschema import validate, SchemaError, FormatChecker
from bson.objectid import ObjectId

scholarships = Blueprint('scholarships', __name__)

@scholarships.route('/scholarships', methods=['GET'])
def get_scholarships():
    """
    list all scholarships in the database.
    """
    scholarship_list = []
    # There eventually should be a limit to how many resources we query.  
    for scholarship in scholarship_collection.find():
        # Convert the ObjectId fields to strings
        scholarship['_id'] = str(scholarship['_id'])
        scholarship_list.append(scholarship)
    return jsonify(scholarship_list)


@scholarships.route('/scholarships', methods=['POST'])
def create_scholarship():
    data = request.get_json()
    try:
        validate(data, scholarship_schema, format_checker=FormatChecker())
    except SchemaError as e:
        return jsonify({'message': f'Schema validation error: {e}'}), 400

    new_scholarship = Scholarship(name=data['name'], description=data['description'], amount=data['amount'], deadline=data['deadline'], url=data['url'])
    create_scholarship_in_db(new_scholarship)
    return jsonify({'message': 'Scholarship created successfully'})
    

@scholarships.route('/scholarships/<scholarship_id>', methods=['GET'])
def get_scholarship(scholarship_id):
    scholarship = read_scholarship_from_db(scholarship_id)
    # Turn to string to avoid Serialize error
    scholarship['_id'] = str(scholarship['_id'])
    return jsonify(scholarship)

@scholarships.route('/scholarships/<scholarship_id>', methods=['PUT'])
def update_scholarship(scholarship_id):
    # Since PUT requests replaces an entire entity, we need to make sure the incoming schema is valid
    data = request.get_json()
    try:
        validate(data, scholarship_schema, format_checker=FormatChecker())
    except SchemaError as e:
        return jsonify({'message': f'Schema validation error: {e}'}), 400

    new_scholarship = Scholarship(name=data['name'], description=None, amount=data['amount'], deadline=data['deadline'], url=data['url'])
    entity_update = update_scholarship_in_db(scholarship_id, new_scholarship)
    
    if entity_update:
        entity_update['_id'] = str(entity_update['_id'])
        return jsonify(entity_update)
    else:
        return jsonify({'message': 'Scholarship not found'}), 400
        
@scholarships.route('/scholarships/<scholarship_id>', methods=['PATCH'])
def patch_scholarship(scholarship_id):
    user_request = request.get_json()
    
    # Make sure request properties are valid for the schema
    # TODO: add type validation for schema request
    try:
        for entry in user_request:
            if entry not in scholarship_schema['properties']:
                raise SchemaError()
    except SchemaError as e:
        return jsonify({'message': f'Schema validation error: {e}'}), 400
    
    updated_scholarship = patch_scholarship_in_db(scholarship_id, user_request)

    # Send user updated resource from db
    if(updated_scholarship):
        response = read_scholarship_from_db(scholarship_id)
        response['_id'] = str(response['_id'])
        return jsonify(response)
    else:
        return jsonify({'message': 'Scholarship not found'}), 400

@scholarships.route('/scholarships/<scholarship_id>', methods=['DELETE'])
def delete_scholarship(scholarship_id):
    deleted_scholarship = delete_scholarship_from_db(scholarship_id)
    if deleted_scholarship:
        deleted_scholarship['_id'] = str(deleted_scholarship['_id'])
        response = jsonify(deleted_scholarship)
        return response
    else:
        return jsonify({'message': 'Scholarship not found'}), 400
