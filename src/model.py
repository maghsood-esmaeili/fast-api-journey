from pydantic import BaseModel

class MongoUser(BaseModel):
    name: str
    email: str

class MongoResponse(MongoUser):
    id: str