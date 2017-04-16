import scrapy

from job.items import Job51Item
from bs4 import BeautifulSoup

class Job51(scrapy.Spider):
    name = "job51"
    allowed_domains = ["search.51job.com"]
    start_urls = [
        u'http://search.51job.com/list/010000,000000,0000,00,9,99,python%20数据,2,1.html',
    ]

    def parse(self, response):
        count = 0
        job_list = BeautifulSoup.findAll("a" , {"class": {"el"}})
        # for job_div in job_list:
        #     print(job_div)

        print("count", count)



