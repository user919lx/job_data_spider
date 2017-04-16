# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Job51Item(scrapy.Item):
    # define the fields for your item here like:
    # 前程无忧数据
    title = scrapy.Field()  # 职位名称
    company = scrapy.Field()  # 公司名称
    location = scrapy.Field()  # 位置
    salary = scrapy.Field()  # 薪水
    url = scrapy.Field() # 详情链接

