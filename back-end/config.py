import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
    MONGO_URI = "mongodb://localhost:27017/db"  # 不使用用户名和密码
