from bson import ObjectId

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from model import MongoUser, MongoResponse
from nosql.database import mongo_database
import project_router

from sql.database import sessionLocal, User

app = FastAPI()

app.include_router(project_router.router)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

user_collection = mongo_database["users"]

@app.get("/")
def greeting():
    return {"Hello": "World"}


@app.get("/users")
async def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@app.get("/all-mongo-users")
async def get_all_mongo_users() -> list[MongoUser]:
    return [user for user in user_collection.find()]

@app.post("/mongodb-add-user")
async def create_mongo_db_user(user: MongoUser):
    result = user_collection.insert_one(
        user.model_dump(exclude_none=True)
    )
    user_response = MongoResponse(
        id=str(result.inserted_id),
        **user.model_dump()
    )
    return user_response

@app.get("/mongodb-get-user/{user_id}")
async def get_user(user_id:str)-> MongoResponse:
    object_id = None
    if ObjectId.is_valid(user_id):
        object_id = ObjectId(user_id)
    
    db_user = user_collection.find_one(
        {
        "_id": object_id
        }
    )
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="user not found"
        )
    user_response = MongoResponse(
        id=str(object_id),
        **db_user
    )
    return user_response

