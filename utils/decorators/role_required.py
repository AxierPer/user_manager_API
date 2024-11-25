from flask_jwt_extended import jwt_required, get_jwt
from flask import jsonify


def role_required(required_role):
    def decorator(fn):
        
        @jwt_required()
        def wrapper(*args, **kwargs):
            claims = get_jwt()
            user_role = claims.get("role", None)
            print("Holi",user_role)
            
            if user_role != required_role:
                return jsonify({"message": "Access denied"}), 403
            
            return fn(*args, **kwargs)
        
        wrapper.__name__ = fn.__name__
        return wrapper
    
    return decorator