from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson import ObjectId
from ..models import get_hotel_collection, get_user_collection

hotel_bp = Blueprint('hotels', __name__, url_prefix='/hotels')

@hotel_bp.route('/', methods=['POST'])
@jwt_required()
def add_hotel():
    current_user = get_jwt_identity()
    user = get_user_collection().find_one({"username": current_user})
    if not user or user.get('role') != 'admin':
        return jsonify({"error": "Admin access required."}), 403

    data = request.get_json()
    name = data.get('name')
    location = data.get('location')
    rating = data.get('rating')
    images = data.get('images')
    description = data.get('description')

    if not name or not location or rating is None or not images or not description:
        return jsonify({"error": "All fields are required."}), 400

    hotel = {
        "name": name,
        "location": location,
        "rating": rating,
        "images": images,
        "description": description
    }

    get_hotel_collection().insert_one(hotel)
    return jsonify({"message": "Hotel added successfully."}), 201

@hotel_bp.route('/', methods=['GET'])
def get_hotels():
    hotel_id = request.args.get('hotel_id')
    if hotel_id:
        hotel = get_hotel_collection().find_one({"_id": ObjectId(hotel_id)})
        if not hotel:
            return jsonify({"error": "Hotel not found."}), 404
        hotel['_id'] = str(hotel['_id'])
        return jsonify(hotel), 200
    else:
        hotels = get_hotel_collection().find().sort("rating", -1)  # 按评分降序排序
        hotel_list = []
        for hotel in hotels:
            hotel['_id'] = str(hotel['_id'])
            hotel_list.append(hotel)
        return jsonify(hotel_list), 200

@hotel_bp.route('/<hotel_id>', methods=['GET'])
def get_hotel(hotel_id):
    hotel = get_hotel_collection().find_one({"_id": ObjectId(hotel_id)})
    if not hotel:
        return jsonify({"error": "Hotel not found."}), 404
    hotel['_id'] = str(hotel['_id'])
    return jsonify(hotel), 200

@hotel_bp.route('/<hotel_id>', methods=['PUT'])
@jwt_required()
def update_hotel(hotel_id):
    current_user = get_jwt_identity()
    user = get_user_collection().find_one({"username": current_user})
    if not user or user.get('role') != 'admin':
        return jsonify({"error": "Admin access required."}), 403

    data = request.get_json()
    update_data = {k: v for k, v in data.items() if v is not None}

    result = get_hotel_collection().update_one({"_id": ObjectId(hotel_id)}, {"$set": update_data})
    if result.matched_count == 0:
        return jsonify({"error": "Hotel not found."}), 404

    return jsonify({"message": "Hotel updated successfully."}), 200
