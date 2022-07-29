import pymongo
from pymongo import MongoClient
import sqlite3
import datetime
def connectMongodb():
    cluster=MongoClient("mongodb+srv://Haithemss:AWHHc0397@tracker.j9kicrx.mongodb.net/?retryWrites=true&w=majority")
    mydb=cluster["Jumia"]
    return mydb["Produits"]
def getData(db,tab):
    data=sqlite3.connect(f"{db}.db")
    cursor=data.cursor()
    cursor.execute(f"Select * from {tab}")
    return cursor.fetchall()
start=datetime.datetime.now()
docs=getData("Tracker","Produits")
collection=connectMongodb()
for doc in docs :
    struct={
        "_id":doc[2],
        "nom":doc[0],
        "lien":doc[1],
        "catégorie":doc[3],
        "image":doc[4],
        "prix":[]
    }
    collection.insert_one(struct)