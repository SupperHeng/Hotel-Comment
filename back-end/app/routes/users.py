from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from ..models import get_user_collection

user_bp = Blueprint('users', __name__, url_prefix='/users')

def validate_username(username):
    # 检查用户名是否为空，长度是否在3到20个字符之间
    if not username or len(username) < 3 or len(username) > 20:
        return False
    return True

def validate_password(password):
    # 检查密码是否为空，长度是否在6到20个字符之间
    if not password or len(password) < 6 or len(password) > 20:
        return False
    return True

def validate_role(role):
    # 确保角色只有 'user' 和 'admin' 两种
    if role not in ['user', 'admin']:
        return False
    return True

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role', 'user')  # 默认角色为 'user'

    if not validate_username(username):
        return jsonify({"error": "Invalid username. It must be between 3 and 20 characters."}), 400

    if not validate_password(password):
        return jsonify({"error": "Invalid password. It must be between 6 and 20 characters."}), 400

    if not validate_role(role):
        return jsonify({"error": "Invalid role. It must be either 'user' or 'admin'."}), 400

    if get_user_collection().find_one({"username": username}):
        return jsonify({"error": "Username already exists."}), 400

    hashed_password = generate_password_hash(password)
    user = {"username": username, "password": hashed_password, "role": role}
    get_user_collection().insert_one(user)

    return jsonify({"message": "User registered successfully."}), 201

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400

    user = get_user_collection().find_one({"username": username})
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"error": "Invalid username or password."}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200
