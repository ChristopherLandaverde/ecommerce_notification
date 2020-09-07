import scrapy
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider,Rule
from itemloaders.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from myproject.items import SFitnessItem

class ProductDetails(scrapy.Spider):
    name = '####'
    #user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'
    allowed_domains=['####']
    start_urls= ['#####']
    rules = (Rule(LinkExtractor(allow_domains=(''),deny_domains=('#####')),callback='parse'))
    
    def __init__(self):
        self.declare_xpath()

    def declare_xpath(self):
        self.getAllCategoriesXpath='####'
        self.getAllSubCategoriesXpath='#####'
        self.getAllItemsXpath='#####'

    def parse(self, response):
        for href in response.xpath(self.getAllCategoriesXpath):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url=url,callback=self.parse_category,dont_filter=True)
 
    def parse_category(self,response):
        for href in response.xpath(self.getAllSubCategoriesXpath):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url,callback=self.sub_category,dont_filter=True)
    
    def sub_category(self,response):
         for href in response.xpath(self.getAllItemsXpath):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url,callback=self.parse_mainitem, dont_filter=True)

            next_page = response.xpath("#####").extract_first()
            if next_page is not None:
             url = response.urljoin(next_page)
             yield scrapy.Request(url, callback=self.sub_category, dont_filter=True)
    

    def parse_mainitem(self,response):

        
        product_loader = ItemLoader(item=SFitnessItem(),response=response)
        product_loader.add_xpath('title','#####')
        product_loader.add_xpath('link','#####')
        product_loader.add_xpath('price','#####')
        product_loader.add_xpath('not_in_stock','#####')
        product_loader.add_xpath('in_stock','#####')
        product_loader.add_xpath('estimated_date_available','####')
        yield product_loader.load_item()
        
        
