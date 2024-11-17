from flask import Flask, request, jsonify
from utils.functions.user import insert_user, delete_user, get_user_id, get_users, update_user

app = Flask(__name__)

@app.route('/user', methods=['POST'])
def user():
    if request.is_json:
        data = request.get_json()
        
        name = data.get('name')
        last_name = data.get('last_name')     
        age = data.get('age')
        email = data.get('email')
        phone = data.get('phone')
        address = data.get('address')
        
        info = insert_user(name=name, last_name=last_name, age=age, email=email, phone=phone, address=address)
        
        return info


@app.route('/user', methods=['GET'])
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