import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from urllib.parse import urljoin
from douban.items import DoubanItem

class doubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = ['https://www.douban.com/tag/%E7%A4%BE%E7%A7%91/book']

    def parse(self, response):  # 提取数据到Items里面，主要用到XPath和CSS选择器提取网页数据
        item = DoubanItem()
        selector = Selector(response)
        Book = selector.xpath('//div[@class="article"]')
        Books = selector.css('dl dd')
        for book in Books:
            item['name'] = book.css('a').xpath('text()').extract()
            item['dataLink'] = book.css('a').xpath('@href').extract()
            item['author'] = book.xpath('div[@class="desc"]/text()').extract()
            item['grade'] = book.xpath('div[@class="rating"]/span/text()').extract()

            print(item['grade'])
            yield item
        nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
        # 第10页是最后一页，没有下一页的链接
        if nextLink:
            nextLink = nextLink[0]
            yield Request(urljoin(response.url, nextLink), callback=self.parse)