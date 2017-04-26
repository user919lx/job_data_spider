# -*- coding: utf-8 -*-
import scrapy


class LagouSpider(scrapy.Spider):
    name = "lagou"
    allowed_domains = ["www.lagou.com"]
    kds = [u'Python']
    kd = kds[0]
    my_url ="https://www.lagou.com/jobs/positionAjax.json?px=default&city=深圳&district=%s&needAddtionalResult=false" % "南山区"
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88?px=default&city=%E6%B7%B1%E5%9C%B3&district=%E5%8D%97%E5%B1%B1%E5%8C%BA",
        "X-Requested-With": "XMLHttpRequest",
        "Host": "www.lagou.com",
        "Connection": "keep-alive",
        "Cookie": "user_trace_token=20160214102121-0be42521e365477ba08bd330fd2c9c72; LGUID=20160214102122-a3b749ae-d2c1-11e5-8a48-525400f775ce; tencentSig=9579373568; pgv_pvi=3712577536; index_location_city=%E5%85%A8%E5%9B%BD; SEARCH_ID=c684c55390a84fe5bd7b62bf1754b900; JSESSIONID=8C779B1311176D4D6B74AF3CE40CE5F2; TG-TRACK-CODE=index_hotjob; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1485318435,1485338972,1485393674,1485423558; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1485423598; _ga=GA1.2.1996921784.1455416480; LGRID=20170126174002-691cb0a5-e3ab-11e6-bdc0-525400f775ce",
        "Origin": "https://www.lagou.com",
        "Upgrade-Insecure-Requests": "1",
        "X-Anit-Forge-Code": "0",
        "X-Anit-Forge-Token": "None",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8"
    }

    cur_page = 1

    def start_requests(self):
        # print(self.my_url)
        # print(self.headers)
        data = {"first":"false","pn":"2","kd":"数据分析师"}
        # print(data)
        return [scrapy.http.FormRequest(self.my_url, headers=(self.headers), formdata=data, callback=self.parse)]

    def parse(self, response):
        print("suss")
        yield
        # print(response.body)
        # print(json.loads(response.body))
        # print(response.body)

