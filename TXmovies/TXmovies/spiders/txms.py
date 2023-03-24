import scrapy
from ..items import TxmoviesItem


class TxmsSpider(scrapy.Spider):
    name = "txms"
    allowed_domains = ["v.qq.com"]
    url = 'https://v.qq.com/x/bu/pagesheet/list?append=1&channel=cartoon&iarea=1&listpage=2&offset={}&pagesize=30'
    offset = 0

    def start_requests(self):
        for i in range(0,121,30):
            url = self.url.format(i)
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response,*args,**kwargs):
        items = TxmoviesItem()
        lists = response.xpath('//div[@class="list_item"]')
        for i in lists:
            items['name'] = i.xpath('./a/@title').get()
            items['description'] = i.xpath('./div/div/title').get()

            yield items

        # if self.offset < 120:
        #     self.offset += 30
        #     url = f'https://v.qq.com/x/bu/pagesheet/list?append=1&channel=cartoon&iarea=1&listpage=2&offset={self.offset}&pagesize=30'
        #
        #     yield scrapy.Request(url=url,callback=self.parse)