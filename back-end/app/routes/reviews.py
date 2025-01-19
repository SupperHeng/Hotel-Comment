from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson import ObjectId
from ..models import get_review_collection, get_user_collection

review_bp = Blueprint('reviews', __name__, url_prefix='/reviews')

@review_bp.route('/', methods=['GET'])
def get_reviews():
    hotel_id = request.args.get('hotel_id')
    if not hotel_id:
        return jsonify({"error": "hotel_id is required."}), 400

    reviews = get_review_collection().find({"hotel_id": ObjectId(hotel_id)})
    review_list = []
    for review in reviews:
        review['_id'] = str(review['_id'])
        review['hotel_id'] = str(review['hotel_id'])
        review['user_id'] = str(review['user_id'])
        review_list.append(review)
    return jsonify(review_list), 200

@review_bp.route('/', methods=['POST'])
@jwt_required()
def add_review():
    hotel_id = request.args.get('hotel_id')
    if not hotel_id:
        return jsonify({"error": "hotel_id is required."}), 400

    current_user = get_jwt_identity()
    user = get_user_collection().find_one({"username": current_user})
    if not user:
        return jsonify({"error": "User not found."}), 404

    data = request.get_json()
    content = data.get('content')
    rating = data.get('rating')

    if not content or rating is None:
        return jsonify({"error": "Content and rating are required."}), 400

    review = {
        "hotel_id": ObjectId(hotel_id),
        "user_id": user['_id'],
        "username": user['username'],
        "content": content,
        "rating": rating
    }

    get_review_collection().insert_one(review)
    return jsonify({"message": "Review added successfully."}), 201

@review_bp.route('/<review_id>', methods=['PUT'])
@jwt_required()
def update_review(review_id):
    current_user = get_jwt_identity()
    user = get_user_collection().find_one({"username": current_user})
    if not user:
        return jsonify({"error": "User not found."}), 404

    review = get_review_collection().find_one({"_id": ObjectId(review_id), "user_id": user['_id']})
    if not review:
        return jsonify({"error": "Review not found or access denied."}), 404

    data = request.get_json()
    update_data = {k: v for k, v in data.items() if v is not None}

    result = get_review_collection().update_one({"_id": ObjectId(review_id)}, {"$set": update_data})
    if result.matched_count == 0:
        return jsonify({"error": "Review not found."}), 404

    return jsonify({"message": "Review updated successfully."}), 200

@review_bp.route('/<review_id>', methods=['DELETE'])
@jwt_required()
def delete_review(review_id):
    current_user = get_jwt_identity()
    user = get_user_collection().find_one({"username": current_user})
    if not user:
        return jsonify({"error": "User not found."}), 404

    review = get_review_collection().find_one({"_id": ObjectId(review_id), "user_id": user['_id']})
    if not review:
        return jsonify({"error": "Review not found or access denied."}), 404

    get_review_collection().delete_one({"_id": ObjectId(review_id)})
    return jsonify({"message": "Review deleted successfully."}), 200
