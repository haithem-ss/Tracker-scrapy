import scrapy
from pymongo import MongoClient
import time

from pymongo import MongoClient
from ..items import Price
class UpdatepricesSpider(scrapy.Spider):
    name = 'UpdatePrices'
    allowed_domains = ['www.jumia.dz']
    start_urls = ['http://www.jumia.dz/']
    def parse(self, response):
        print(collection.find({},"lien"))
        
