import scrapy
import re
from job.items import Job51Item
from bs4 import BeautifulSoup
from datetime import datetime

class Job51(scrapy.Spider):
    name = "job51"
    allowed_domains = ["search.51job.com", "jobs.51job.com"]
    start_urls = [
        u'http://search.51job.com/list/040000,000000,0000,00,9,99,数据,2,1.html',
    ]
    count = 0
    id_pattern = re.compile(".*/(\d+)\.html.*")

    def parse(self, response):
        bs_obj = BeautifulSoup(response.body, "html5lib")
        job_list = bs_obj.find_all("p", {"class": {"t1"}})
        for job_div in job_list:
            job_url = job_div.a.attrs['href']
            # print(job_div.prettify())
            # print("-------------------------------------")
            yield scrapy.http.Request(job_url,callback=self.parse_page)
            # print("====================================")

    def parse_page (self, response):
        bs_obj = BeautifulSoup(response.body, "html5lib")
        ds1 = bs_obj.find("div", {'class': 'cn'})
        item = Job51Item()
        item['url'] = response.url
        item['title'] = bs_obj.h1.text
        item['location'] = ds1.span.text
        item['salary'] = ds1.strong.text
        item['company'] = ds1.p.a.text
        ds2 = [x for x in bs_obj.find('div',{'class': 't1'}).find_all('span')]
        ds2_dict = {'i1': 'experience', 'i2': 'education', 'i3': 'number', 'i4': 'release_at'}
        for x in ds2:
            item_key = ds2_dict.get(x.em.attrs['class'][0])
            if item_key is not None:
                item[item_key] = x.text
        self.count = self.count + 1
        item['job_desc'] = bs_obj.find("div", {'class': 'job_msg'}).text.replace('\t', '')
        item['spider_at'] = datetime.now()

        m = re.match(self.id_pattern, item['url'])

        print("count", self.count)
        yield item
