import scrapy

from job.items import JobItem


class JobSpider(scrapy.Spider):
    name = "job"
    allowed_domains = ["search.51job.com"]
    start_urls = [
        "http://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html",
    ]

    def parse(self, response):
        count = 0
        for sel in response.xpath('//*[@id="resultList"]/div[@class="el"]'):
            count = count+1
            item = JobItem()
            item['title'] = sel.xpath('p/span/a/@title').extract()[0]
            item['company'] = sel.xpath('span/a/@title').extract()[0]  # 公司名称
            item['location'] = sel.xpath('span[@class="t3"]/text()').extract()[0]  # 位置
            item['salary'] = sel.xpath('span[@class="t3"]/text()').extract()[0]  # 薪水
            # print(item)
            yield item
        print("count", count)
