from .base import Session, User, select, UUID

def check_user_exists(session: Session, email=None, username=None):
    if email:
        if session.exec(select(User).where(User.email == email)).first():
            return "Email already registered"
    
    if username:
        if session.exec(select(User).where(User.username == username)).first():
            return "Username already taken"
    
    return None

def check_uuid(uuid_val) -> bool:
    
    try:
        u = UUID(uuid_val)
        
        return u.version == 7
    
    except ValueError:
        return False