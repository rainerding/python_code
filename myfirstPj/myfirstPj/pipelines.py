# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BaiduPipeline(object):
    # 爬取网页
    def process_item(self, item, spider):
        return item

class BaiduMysqlPipeline(object):
    # 爬取网页后存入数据库
    def process_item(self, item, spider):
        return item