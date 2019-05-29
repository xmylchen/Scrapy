# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings

class DoubanPipeline(object):
   # def process_item(self, item, spider):
   #     return item
   def __init__(self):
       host = settings["MONGODB_HOST"]
       port = settings["MONGODB_PORT"]
       dbname = settings["MONGODB_DBNAME"]
       sheetname = settings["MONGODB_SHEETNAME"]
       # 创建MONGODB数据库链接
       client = pymongo.MongoClient('mongodb://douban:douban@localhost:27017/douban')
       # 指定数据库
       mydb = client[dbname]
       # 存放数据的数据库表名
       self.post = mydb[sheetname]

   def process_item(self, item, spider):
       data = dict(item)
       self.post.insert(data)
       return item