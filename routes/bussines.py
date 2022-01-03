from fastapi import APIRouter
from config.db import conn
from models.bussines import Bussines
from schemas.bussines import bussinesModel, bussinesModel_list
from bson import ObjectId

bussines = APIRouter()
@bussines.get("/")
async def root():
    return {"message": "Hello World from fastApi"}

@bussines.get('/bussines', tags=["Bussines"])
async def get_bussines():
    try:
        return bussinesModel_list(conn.Bussiness.Place.find())
    except:
        return "Server error"

@bussines.post('/create_bussines', tags=["Bussines"])
async def create_bussines(bussines: Bussines):
    try:
        new_bussines = dict(bussines)
        del new_bussines["id"]
        conn.Bussiness.Place.insert_one(new_bussines)
        return {"ok":True}
    except:
        return {"ok":False}

@bussines.put('/update_bussines/{id}', tags=["Bussines"])
async def update_bussines(id: str, bss: Bussines):
    try:
        conn.Bussiness.Place.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(bss)})
        return {"ok":True}
    except:
        return {"ok":False}

@bussines.delete('/delete_bussines/{id}', tags=["Bussines"])
async def delete_bussines(id: str):
    try:
        bussinesModel(conn.Bussiness.Place.find_one_and_delete({"_id": ObjectId(id)}))
        return {"ok":True}
    except:
        return {"ok":False}

