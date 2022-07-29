

from scrapy.item import Item, Field  
import scrapy  


class TrackerItem(scrapy.Item):
    titre = scrapy.Field() 
    lien = scrapy.Field() 
    SKU = scrapy.Field() 
    Catégorie = scrapy.Field() 
    image = scrapy.Field() 
    prix=scrapy.Field()
    promotion = scrapy.Field() 
    prix_promotion = scrapy.Field()
    date=scrapy.Field()
    taux_promotion= scrapy.Field()


class Catégore(scrapy.Item):
    title = scrapy.Field() 
    lien = scrapy.Field()
class Price(scrapy.Item):
    pass