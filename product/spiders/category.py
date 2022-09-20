import scrapy


class AnalogSpider(scrapy.Spider):
    name = 'analog'
    allowed_domains = ['analog.com']
    start_urls = ['http://analog.com/']

    def parse(self, response):
        pass
