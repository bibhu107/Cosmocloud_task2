from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from .routers import user_router, org_router

app = FastAPI()

# Configure CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure database connection
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

# Mount routers
app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(org_router, prefix="/org", tags=["org"])
