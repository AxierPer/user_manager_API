from email_validator import validate_email, EmailNotValidError

def validate_data(func):
    
    def wrapper(*args, **kwargs):
        name = kwargs.get('name') or args[0]
        last_name = kwargs.get('last_name') or args[1]
        age = kwargs.get('age') or args[2]
        email = kwargs.get('email') or args[3]
        phone = kwargs.get('phone') or args[4]
        address = kwargs.get('address') or args[5]
        username = kwargs.get('username') or args[6]
        role = kwargs.get('role') or args[7]
        password = kwargs.get('password') or args[8]
        
        if not name or len(name) < 3:
            raise ValueError("The name must be at least 3 characters long")
        
        if not username or len(username) < 3:
            raise ValueError("The username must be at least 3 characters long")
        
        if not role or len(role) < 3:
            raise ValueError("The role must be at least 3 characters long")
        
        if not password or len(password) < 3:
            raise ValueError("The password must be at least 3 characters long")
        
        if not last_name or len(last_name) < 3:
            raise ValueError("The last name must be at least 3 characters long")
        
        if not age or age <= 0 or age >= 99:
            raise ValueError("The age is not valid")
        
        try:
            validate_email(email)
            
        except EmailNotValidError as e:
            raise ValueError(f"El correo electrónico '{email}' no es válido: {e}")
        
        phone_str = str(phone)
        if not phone or len(phone_str) < 10:
            raise ValueError("The phone number is not valid")
        
        if not address or len(address) < 10:
            raise ValueError("The address is not valid.")

        return func(*args, **kwargs)
    
    return wrapper