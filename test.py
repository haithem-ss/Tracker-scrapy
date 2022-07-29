import pymongo
from pymongo import MongoClient
from bson import ObjectId
import sqlite3
import datetime
from datetime import date
def connectMongodb():
    cluster=MongoClient("mongodb+srv://Haithemss:AWHHc0397@tracker.j9kicrx.mongodb.net/?retryWrites=true&w=majority")
    mydb=cluster["Jumia"]
    return mydb["Produits"]
collection=connectMongodb()
items=collection.find({})
i=1
for item in items :
    try :
        collection.update_one({"_id":item["_id"]},
        {"$set":{"Historique":[item["Historique"]]}
        ,'$unset': {'prix': ""}})
    except Exception:
        collection.update_one({"_id":item["_id"]},
        {'$unset': {'prix': ""}})
    finally :
        print(f"Item number {i}",end="\r")
        i+=1