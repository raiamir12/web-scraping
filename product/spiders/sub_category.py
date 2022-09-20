import scrapy


class SubCategorySpider(scrapy.Spider):
    name = 'sub_category'
    allowed_domains = ['www.st.com']
    start_urls = ['http://www.st.com/']

    def parse(self, response):
        pass
