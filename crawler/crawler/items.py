# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose

class CrawlerItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    date_last = scrapy.Field()


class CrawlItemLoader(ItemLoader):
    url_out = TakeFirst()
    # url_out = MapCompose()