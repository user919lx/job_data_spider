# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class Job51Item(Item):
    # define the fields for your item here like:
    # 前程无忧数据
    title = Field()  # 职位名称
    company = Field()  # 公司名称
    location = Field()  # 位置
    salary = Field()  # 薪水
    url = Field()  # 详情链接
    experience = Field()  # 工作经验
    education = Field()  # 学历
    number = Field()  # 人数
    job_desc = Field()  # 职位描述
    job_id = Field()  # 51job上的id
    release_at = Field()  # 职位发布时间
    spider_at = Field()  # 爬取时间


