from utils.decorators.users import validate_data
from utils.classes.user import UserClass

@validate_data
def insert_user( name,last_name, age, email, phone, address, username, role, password):
    user = UserClass()
    insert = user.insert_user(name=name,last_name=last_name, age=age, email=email, phone=phone, address=address, username=username, role=role, password=password)
    return insert

@validate_data
def update_user(name, last_name, age, email, phone, address,id,username, role, password):
    user = UserClass()
    update = user.update_user(id=id, name=name, last_name=last_name, age=age, email=email, phone=phone, address=address, username=username, role=role, password=password)
    return update

def get_users():
    user = UserClass()
    users = user.get_users()
    return users

def get_user_id(id):
    user = UserClass()
    user_id = user.get_user_id(id)
    return user_id

def delete_user(id):
    user = UserClass()
    delete = user.delete_user(id)
    return delete