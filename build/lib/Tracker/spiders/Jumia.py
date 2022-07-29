import scrapy
from ..items import TrackerItem , Catégore
class JumiaSpider(scrapy.Spider):
    name = 'Jumia'
    allowed_domains = ['www.jumia.dz']
    start_urls = ['https://www.jumia.dz/epicerie']
    page=0
    def parseCats(self, response):

        pass
    def parse(self, response): 
        items=TrackerItem()
        nb=response.css(".-gy5.-phs::text").extract()
        nb=int(nb[0].split(" ")[0])
        items['Catégorie']="epicerie"
        items['titre']=response.css(".info .name ::text").extract()
        items['lien']=response.css(".c-prd .core::attr(href)").extract()
        items['image']=response.css(".img-c .img::attr(data-src)").extract()
        yield items
        nextp=f"https://www.jumia.dz/epicerie/?page={JumiaSpider.page}"
        if nb // 30 :
            JumiaSpider.page+=1
            yield response.follow(nextp,callback=self.parse)
    def parseProduct(self,response):
        pass