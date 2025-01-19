from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from config import Config
from app.models import mongo  # 确保导入 mongo 对象
from app.init_db import initialize_database  # 导入初始化数据库函数

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    mongo.init_app(app)  # 初始化 mongo

    from app.routes.hotels import hotel_bp
    from app.routes.users import user_bp  # 添加用户蓝图
    from app.routes.reviews import review_bp  # 添加评论蓝图
    app.register_blueprint(hotel_bp)
    app.register_blueprint(user_bp, url_prefix='/users')  # 注册用户蓝图，并添加前缀
    app.register_blueprint(review_bp, url_prefix='/reviews')  # 注册评论蓝图，并添加前缀

    app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # 替换为你的 secret key
    app.config['JWT_TOKEN_LOCATION'] = ['headers']  # 指定 JWT token 的位置

    jwt = JWTManager(app)  # 初始化 JWTManager

    with app.app_context():
        initialize_database()  # 初始化数据库

    return app