from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class Myspider(CrawlSpider):
    name='CrawTest'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://www.mzitu.com/']
    rules={
        Rule(LinkExtractor(allow='http://www.mzitu.com/\d{1,6}',
                           deny=('http://www.mzitu.com/\d{1,6}/\d{1,6}')),
             callback='parse_item',follow=True),
    }
    def parse_item(self,response):
        print(response.url)

