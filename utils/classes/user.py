from database.sessions import get_db
import json
from database.models import User
from flask import jsonify

class UserClass:
    def insert_user(self,name, last_name, age, email, phone, address,username, role, password):
        
        db = next(get_db())
        new_user = User(name=name, last_name=last_name, age=age, email=email, phone=phone, address=address, username=username, role=role, password=password) 
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        return jsonify({
            "message":f"User {name} add successfull"
        })
    
    
    def get_users(self):
        db = next(get_db())
        users = db.query(User).all()

        data_list = []
        for user in users:
            user_dict = {column.name: getattr(user, column.name) for column in user.__table__.columns}
            data_list.append(user_dict)

        users_format =  json.dumps(data_list, indent=4)
        
        return users_format 
    
    
    def get_user_id(self, id):
        db = next(get_db())
        users = db.query(User).where(User.id == id)
        data_list = []
        for user in users:
            user_dict = {column.name: getattr(user, column.name) for column in user.__table__.columns}
            data_list.append(user_dict)

        users_format =  json.dumps(data_list, indent=4)
        
        if data_list == []:
            return jsonify({
                "message":f"User with id: {id} is don't exist"
                })
        
        return users_format    
    
    def delete_user(self, id):
        db = next(get_db())
        user_delete = db.query(User).where(User.id == id).delete()
        
        if user_delete == 0:
            return jsonify({
                "message":f"The user whith id: {id} is don't exist"
                })
        
        db.commit()
        
        return jsonify({
            "message":f"User {id} deleted."
            })
    
    
    def update_user(self,id, name=None, last_name=None, age=None, email=None, phone=None, address=None, username=None, role= None, password=None):
        db = next(get_db())
        user_update = db.query(User).where(User.id == id).first()
        
        if user_update:
            if name:
                user_update.name = name

            if last_name:
                user_update.last_name = last_name

            if age is not None:
                user_update.age = age

            if email:
                user_update.email = email

            if phone is not None:
                user_update.phone = phone

            if address:
                user_update.address = address
            
            if username:
                user_update.username = username
            
            if role:
                user_update.role = role
            
            if password:
                user_update.password = password

            db.commit()

            db.refresh(user_update)

            return jsonify({
                "message":f"Usuario con ID {id} actualizado exitosamente."
                })
            
        else:
            return jsonify({
                "message":f"Usuario con ID {id} no encontrado."
                })