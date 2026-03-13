from flask import Blueprint, request, jsonify
from BACKEND.utils.db import DBHelper

profile_bp = Blueprint('profile', __name__)
db = DBHelper()

@profile_bp.route('/<int:user_id>', methods=['GET'])
def get_profile(user_id):
    user = db.get_user_by_id(user_id)
    return jsonify(user.to_dict()) if user else jsonify({"message": "User not found"}), 404

@profile_bp.route('/<int:user_id>', methods=['PUT'])
def update_profile(user_id):
    data = request.json
    result = db.update_user(user_id, data)
    return jsonify(result)

@profile_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_profile(user_id):
    result = db.delete_user(user_id)
    return jsonify(result)