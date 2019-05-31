# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #名称
    name = scrapy.Field()
    #书籍连接
    dataLink = scrapy.Field()
    #评分
    grade = scrapy.Field()
    #作者
    author = scrapy.Field()
    #类别
    category = scrapy.Field()
