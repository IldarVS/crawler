from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from crawler.items import CrawlItemLoader, CrawlerItem


class NameSpider(CrawlSpider):
    name = 'spider_name'

    allowed_domains = ['geekbrains.ru']
    start_urls = ['https://geekbrains.ru/courses']

    rules = (
        Rule(LinkExtractor(
        restrict_xpaths=['//div[@class="searchable-container"]'],
            allow = r'https://geekbrains.ru/\w+/\d+$'
        ), 'parse_item'
        ),
    )

    def parse_item(selfself, response):
        selector = Selector(response)
        l = CrawlItemLoader(CrawlerItem(), selector)
        l.add_value('url', response.url)
