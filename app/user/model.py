from datetime import datetime
from pydantic import BaseModel
from pymongo.collection import Collection

class User(BaseModel):
    id: str
    name: str
    email: str
    created_at: datetime = None
    updated_at: datetime = None

    class Config:
        orm_mode = True


def create_user(db: Collection, user: User) -> User:
    user_dict = user.dict()
    user_dict.update({
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    })
    result = db.insert_one(user_dict)
    user.id = str(result.inserted_id)
    return user

def get_users(db: Collection, limit: int = 100, skip: int = 0, name: str = None):
    query = {}
    if name:
        query = {"name": {"$regex": name, "$options": "i"}}
    users = db.find(query, limit=limit, skip=skip)
    total = db.count_documents(query)
    return users, total

def get_user(db: Collection, user_id: str) -> User:
    user = db.find_one({"_id": ObjectId(user_id)})
    if user:
        return User(**user)

    return None
