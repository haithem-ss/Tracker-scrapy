import scrapy
from ..items import Catégore


class CountitemsSpider(scrapy.Spider):
    name = 'countitems'
    allowed_domains = ['www.jumia.dz']
    start_urls = ['http://www.jumia.dz/']

    def parse(self, response):
        pass
