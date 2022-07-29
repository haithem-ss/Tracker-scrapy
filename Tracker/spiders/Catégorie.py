from gc import callbacks
from re import T
import time
import scrapy
from ..items import Catégore , TrackerItem
from .Jumia import JumiaSpider
from datetime import date
import sqlite3
class CatégorieSpider(scrapy.Spider):
    name = 'Catégorie'
    allowed_domains = ['www.jumia.dz']
    start_urls = ['http://www.jumia.dz/']
    global urls
    urls={}     
    number=0   
    def parse(self, response):
        # a=response.css(".flyout .itm span::text").extract()
        # b=response.css(".flyout .itm::attr(href)").extract()
        # for j in b:
        #     # cat['Nbrproduits']=int(response.css(".-gy5.-phs::text").extract()[0].split(" ")[0])
        #     yield response.follow(j,callback=self.parsecat)
        yield response.follow("/all-products/",callback=self.parsecat)

    def parsecat(self, response):
        # a=response.css(".-phxl::text").extract()
        b=response.css(".-phxl::attr(href)").extract()
        nb=response.css(".-gy5.-phs::text").extract()
        nb=int(nb[0].split(" ")[0])
        # cont=True
        liste=[]
        for x in b:
            if nb< 1900 or x in response.request.url:
                yield response.follow(x,callback=self.parseProduct)
            else:
                liste.append(x)
        # if cont :
        for j in liste:
            yield response.follow(j,callback=self.parsecat)
    def parseProduct(self,response):
        for page in range(1, 51):
            for product in response.css(".c-prd .core::attr(href)").extract() :
                yield response.follow(product,callback=self.parseProductInfo)
            yield response.follow(f"?page={page}",callback=self.parseProduct)
    def parseProductInfo(self,response):
        item=TrackerItem()
        item['titre']=response.css(".-pts.-pbxs ::text").get()
        item['lien']=response.request.url
        item['SKU']=response.css(".-lsn .-pvxs:nth-child(1)::text").extract()[0][2:]
        item['Catégorie']=response.css(".cbs:nth-child(2) ::text").get()
        item['image']=response.css("#imgs a.itm img ::attr(data-src)").get()
        item['prix_promotion']=response.css(".-fs24::text").get()
        item["date"]=str(date.today())
        item["prix"]=response.css(".-lthr::text").get()
        item["taux_promotion"]=response.css("._dyn::text").get()
        if item["taux_promotion"] is not None and item["prix_promotion"] is not None:
            item["promotion"]=True
        else: 
            item['prix_promotion'],item['prix']=item['prix'],item['prix_promotion']
            item["promotion"]=False
        print("item number ",CatégorieSpider.number,end="\r")
        CatégorieSpider.number+=1
        yield item