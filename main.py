from flask import Flask, request, jsonify
import json
from utils.functions.user import insert_user, delete_user, get_user_id, get_users, update_user
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from config.config import JWT_SECRET_KEY
from flask_cors import CORS
from datetime import timedelta
from utils.decorators.role_required import role_required

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
jwt = JWTManager(app)

cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

@app.route('/login', methods=['POST'])
def login():
    if request.json:
        data = request.get_json()
        
        username = data.get('username')
        password = data.get('password')
        
        user = json.loads(get_users())
        print(user[0]["password"])
        
        if user and user[0]["password"] == password:
            access_token = create_access_token(
                identity=username,
                additional_claims = {"role": user[0]["role"]},
                expires_delta=timedelta(minutes=2)
            )
        return jsonify(access_token = access_token),200
    
    return jsonify({"message": "User or Password not valid"}), 401


@app.route('/user', methods=['POST'])
@role_required("admin")
def user():
    if request.is_json:
        data = request.get_json()
        
        name = data.get('name')
        last_name = data.get('last_name')     
        age = data.get('age')
        email = data.get('email')
        phone = data.get('phone')
        address = data.get('address')
        username = data.get('username')
        role = data.get('role')
        password =  data.get('password')
        
        info = insert_user(name=name, last_name=last_name, age=age, email=email, phone=phone, address=address, username=username, role=role, password=password)
        
        return info


@app.route('/user', methods=['GET'])
@role_required("admin")
def get_user():
    data = get_users()
    
    return data

@app.route('/user/<int:id>', methods=['GET'])
def get_user_by_id(id):
    user = get_user_id(id)
    
    return user


@app.route('/user/<int:id>', methods=['DELETE'])
def delete_users(id):
    info = delete_user(id)
    
    return info


@app.route('/user/<int:id>', methods=['PUT'])
def update_users(id):
    if request.is_json:
        data = request.get_json()
        
        name = data.get('name')
        last_name = data.get('last_name')
        age = data.get('age')
        email = data.get('email')
        phone = data.get('phone')
        address = data.get('address')
        
        info = update_user(id=id,name=name, last_name=last_name, age=age, email=email, phone=phone, address=address)
        
        return info

        
    return ""

if __name__ == '__main__':
    app.run(debug=True)