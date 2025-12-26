from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import User, sessionLocal
app = FastAPI()


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

class UserBody(BaseModel):
    name: str
    email: str


@app.post("/user")
async def create_user(
    user: UserBody,
    db: Session = Depends(get_db)
):
    new_user = User(
        name = user.name,
        email = user.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/users/{user_id}")
async def get_user_by_user_id(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = (
        db.query(User).filter(
            User.id == user_id
        ).first()
    )
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail="User Not Found"
        )
    return user

@app.post("/user/{user_id}")
async def update_user(user_id: int, user: UserBody, db: Session = Depends(get_db)):
    db_user = (
        db.query(User).filter(
            User.id == user_id
        ).first()

    )
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail="User Not Found"
        )
    db_user.name = user.name
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return user

@app.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = (
        db.query(User).filter(
            User.id == user_id
        ).first()

    )
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail="User Not Found"
        )
    db.delete(db_user)
    db.commit()
    return {"detail": f"User {db_user.name} deleted"}
     

