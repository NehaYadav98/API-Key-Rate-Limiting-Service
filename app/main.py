from fastapi import FastAPI, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from . import crud
from .rate_limiter import check_rate_limit

Base.metadata.create_all(bind=engine)

app = FastAPI()

# DB connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Generate API key
@app.post("/generate-key")
def generate_key(db: Session = Depends(get_db)):
    return crud.create_api_key(db)

# Protected API
@app.get("/protected")
def protected_api(
    x_api_key: str = Header(...),
    db: Session = Depends(get_db)
):
    db_key = crud.get_api_key(db, x_api_key)

    if not db_key:
        raise HTTPException(status_code=403, detail="Invalid API Key")

    if not check_rate_limit(x_api_key):
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    return {"message": "Access granted ✅"}