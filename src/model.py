from pydantic import BaseModel, EmailStr, field_validator


class Tweet(BaseModel):
    content: str
    hastags: list[str]

class MongoUser(BaseModel):
    name: str
    email: EmailStr
    age: int
    tweets: list[Tweet] | None = None
    @field_validator("age")
    def validate_age(cls, value):
        
        if value < 18 or value > 100:
            raise ValueError("This aged quys is not acceptable")
        return value


class MongoResponse(MongoUser):
    id: str