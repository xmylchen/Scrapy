import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from urllib.parse import urljoin
from douban.items import DoubanItem
from scrapy_redis.spiders import RedisSpider

class doubanSpider(RedisSpider):
    name = "douban"
    allowed_domains = ["douban.com"]
    #start_urls = ['https://book.douban.com/tag/%E5%8E%86%E5%8F%B2']
    redis_key = 'douban:start_urls'

    def parse(self, response):  # 提取数据到Items里面，主要用到XPath和CSS选择器提取网页数据
        item = DoubanItem()
        selector = Selector(response)
        Book = selector.xpath('//div[@class="info"]')
        category = selector.xpath('//div[@id="content"]').xpath('h1/text()').extract()
        for book in Book:
            item['name'] = book.xpath('h2/a/text()').extract()
            item['dataLink'] = book.xpath('h2/a/@href').extract()
            item['author'] = book.xpath('div[@class="pub"]/text()').extract()
            item['grade'] = book.xpath('div[@class="star clearfix"]/span/text()').extract()
            item['category'] = category
            yield item
        nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
        # 第10页是最后一页，没有下一页的链接
        if nextLink:
            nextLink = nextLink[0]
            yield Request(urljoin(response.url, nextLink), callback=self.parse)