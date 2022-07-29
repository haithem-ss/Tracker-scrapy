# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .items import Catégore ,TrackerItem
class TrackerPipeline:
    def __init__(self):
        # self.create_connection()
        # self.create_table()
        self.connectMongodb()

    def connectMongodb(self):
        cluster=MongoClient("mongodb+srv://Haithemss:AWHHc0397@tracker.j9kicrx.mongodb.net/?retryWrites=true&w=majority")
        mydb=cluster["Jumia"]
        self.collection=mydb["Produits"]
    # def create_connection(self):
    #     self.collection=sqlite3.connect("Tracker.db")
    #     self.cursor=self.conn.cursor()
    # def create_table(self):
    #     self.cursor.execute("""Drop table if exists Catégories""")
    #     self.cursor.execute("""Drop table if exists Produits""")
    #     self.cursor.execute("""CREATE TABLE Catégories (title TEXT UNIQUE,lien TEXT UNIQUE)""")
    #     self.cursor.execute("""CREATE TABLE Produits (titre TEXT UNIQUE,lien TEXT UNIQUE,sku TEXT UNIQUE , Catégore TEXT , image TEXT)""")
    def process_item(self, item, spider):
        self.storedb(item)
        return item
    def storedb(self,doc):

        res=self.collection.update_one(        
            {"_id":doc["SKU"]},
        {"$set":{            
            "nom":doc["titre"],
            "lien":doc["lien"],
            "catégorie":doc["Catégorie"],
            "image":doc["image"],
            },
            "$push":{            
                "Historique":{
                "prix":doc["prix"],
                "promotion":doc["promotion"],
                "prix_promotion":doc["prix_promotion"],
                "date":doc["date"]
            }}
        },
        upsert=True)
        # if isinstance(item,Catégore):
        #     self.cursor.execute("""INSERT INTO Catégories VALUES(?,?);""", (item['title'], item['lien']))
        # if isinstance(item,TrackerItem):
        #     self.cursor.execute("""INSERT INTO Produits VALUES(?,?,?,?,?);""", (item['titre'], item['lien'],item['SKU'], item['Catégorie'],item['image']))
        # self.conn.commit()