from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from CrwalProject.items import CrwalprojectItem
from scrapy import Request

#我得测试
class Myspider(CrawlSpider):
    name='CrawTest'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://www.mzitu.com/']
    img_urls=[]
    rules={
        Rule(LinkExtractor(allow='http://www.mzitu.com/\d{1,6}',
                           deny=('http://www.mzitu.com/\d{1,6}/\d{1,6}')),
             callback='parse_item',follow=True),
    }
    def parse_item(self,response):
        item=CrwalprojectItem()
        max_num=response.xpath("descendant::div[@class='main']/div[@class='content']/"
                               "div[@class='pagenavi']/a[last()-1]/span/text()").extract_first()
        name= response.xpath("./*//div[@class='main']/div[1]/h2/text()").extract_first(default="N/A")
        item['name']=name
        for num in range(1,int(max_num)):
            page_url=response.url+'/'+str(num)
            yield Request(page_url,callback=self.img_url)
        item['image_urls']=self.img_urls
        yield item

    def img_url(self,response):
        img_urls=response.xpath("descendant::div[@class='main-image']/descendant::img/@src").extract()
        for img_url in img_urls:
            self.img_urls.append(img_url)





