# coding=utf-8   #
import requests
import json
import sys
import io
import codecs
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

def get_header():
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE?px=default&gj=%E5%BA%94%E5%B1%8A%E6%AF%95%E4%B8%9A%E7%94%9F,3%E5%B9%B4%E5%8F%8A%E4%BB%A5%E4%B8%8B&city=%E6%B7%B1%E5%9C%B3",
        "X-Requested-With": "XMLHttpRequest",
        "Host": "www.lagou.com",
        "Connection":"keep-alive",
        "Cookie":"user_trace_token=20161024133200-2ff222f8-99ab-11e6-b147-5254005c3644; LGUID=20161024133200-2ff227d7-99ab-11e6-b147-5254005c3644; RECOMMEND_TIP=true; gr_user_id=16f22b68-e3fb-43b0-8899-3c748db9ea2b; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=32; index_location_city=%E6%B7%B1%E5%9C%B3; JSESSIONID=43B7075E7414440076CF5D8DE77724D7; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1493063845,1493091836,1493179151,1493239773; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1493239773; _gat=1; LGSID=20170427044935-db160460-2ac1-11e7-b3d3-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%25E5%25B8%2588%3Fpx%3Ddefault%26city%3D%25E6%25B7%25B1%25E5%259C%25B3%26district%3D%25E5%258D%2597%25E5%25B1%25B1%25E5%258C%25BA; LGRID=20170427044935-db160664-2ac1-11e7-b3d3-5254005c3644; _ga=GA1.2.1400412814.1477287129; _gid=GA1.2.213168506.1493239773; _putrc=C0A1C6352884E53D; SEARCH_ID=12e422585664400c9c52a418f6cc2b58",
        "Origin": "https://www.lagou.com",
        "Upgrade-Insecure-Requests":"1",
        "X-Anit-Forge-Code": "0",
        "X-Anit-Forge-Token": "None",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8"
        }
    return headers


def get_form(i):
    data = {"first":"false","pn":i,"kd":"数据"}
    return(data)


def store(data,index):
    filename = "lagou_json_data_"+str(index)+".json"
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


def store(text, index):
    filename = "job_lists/lagou_json_data_" + str(index) + ".json"
    file = codecs.open(filename, "w", "utf-8-sig")
    file.write(text)
    file.close()

url_lists = ["https://www.lagou.com/jobs/positionAjax.json?gj=%E5%BA%94%E5%B1%8A%E6%AF%95%E4%B8%9A%E7%94%9F%2C3%E5%B9%B4%E5%8F%8A%E4%BB%A5%E4%B8%8B&px=default&city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false"]
s = requests.Session()
for i in range(1, 21):
    resp = s.post(url_lists[0], data=get_form(i), headers=get_header())
    rtb = json.loads(resp.text)
    rtb = json.dumps(rtb, indent=4, ensure_ascii=False)
    print(i)
    # print(rtb)
    store(rtb, i)

s.close()
