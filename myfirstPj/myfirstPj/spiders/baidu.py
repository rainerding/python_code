import scrapy


class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["www.baidu.com"]
    start_urls = ["http://www.baidu.com/"]

    def parse(self, response,*args,**kwargs):
        tile = response.xpath('//html/head/title/text()')
        print(tile)
