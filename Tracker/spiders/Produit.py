import scrapy
from ..items import TrackerItem

class ProduitSpider(scrapy.Spider):
    name = 'Produit'
    allowed_domains = ['www.jumia.dz']
    start_urls = ['http://www.jumia.dz/']

    def parse(self, response):
        pass
