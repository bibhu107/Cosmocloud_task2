# organization/model.py
from pydantic import BaseModel

class Organization(BaseModel):
    name: str


# organization/controller.py
from fastapi import APIRouter, HTTPException
from typing import List
from .model import Organization
from bson.objectid import ObjectId
from pymongo import MongoClient

router = APIRouter()

client = MongoClient("mongodb://localhost:27017")
db = client["mydatabase"]
collection = db["organizations"]

@router.post("/organizations/")
async def create_organization(org: Organization):
    org_dict = org.dict()
    org_dict['_id'] = ObjectId()
    collection.insert_one(org_dict)
    return { "message": "Organization created successfully." }

@router.get("/organizations/", response_model=List[Organization])
async def list_organizations(offset: int = 0, limit: int = 100, name: str = ""):
    cursor = collection.find({ "name": { "$regex": name } }).skip(offset).limit(limit)
    organizations = [Organization(**org) for org in cursor]
    total_count =
