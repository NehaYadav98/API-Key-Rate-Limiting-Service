from sqlalchemy.orm import Session
from .models import APIKey
from .auth import generate_api_key

def create_api_key(db: Session):
    key = generate_api_key()
    db_key = APIKey(key=key)
    db.add(db_key)
    db.commit()
    db.refresh(db_key)
    return db_key

def get_api_key(db: Session, key: str):
    return db.query(APIKey).filter(APIKey.key == key).first()