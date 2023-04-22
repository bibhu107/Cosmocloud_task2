from fastapi import APIRouter, Depends
from pymongo.collection import Collection
from ..dependencies import get_db
from .model import User
from .schema import UserCreate, UserOut, UserList

user_router = APIRouter()

@user_router.post("/", response_model=UserOut)
async def create_user(user: UserCreate, db: Collection = Depends(get_db)):
    created_user = create_user(db, User(**user.dict()))
    return created_user

@user_router.get("/", response_model=UserList)
async def read_users(limit: int = 100, skip: int = 0, name: str = None, db: Collection = Depends(get_db)):
    users, total = get_users(db, limit=limit, skip=skip, name=name)
    return {"total": total, "items": users}

@user_router.get("/{user_id}", response_model=UserOut)
async def read_user(user_id: str, db: Collection = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
