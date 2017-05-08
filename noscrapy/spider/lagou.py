import requests
import json
import codecs
import os
kd = "数据工程"  # 搜索关键词
url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
dir_path = "../temp/json/kd_"+kd
if not os.path.exists(dir_path):
    os.makedirs("../temp/json/kd_" + kd)


def store(text, index):
    filename = dir_path+"/lagou_json_data_" + str(index) + ".json"
    file = codecs.open(filename, "w", "utf-8-sig")
    file.write(text)
    file.close()


i = 1
while True:
    print("i="+str(i))
    resp = requests.post(url, data={"first": "false", "pn": i, "kd": kd})
    # try:
    rtb = json.loads(resp.text)
    count = rtb['content']['positionResult']['totalCount']
    rtb = json.dumps(rtb, indent=4, ensure_ascii=False)
    store(rtb, i)
    if i*15 >= count:
        break
    else:
        i = i+1
    # except BaseException:
    #     print("error")
    #     print("resp", resp)
    #     print("resp.text", resp.text)




#
# def get_header():
#     headers = {
#         "User-Agent": '''Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CL
#         R 2.0.50727)''',
#         "Accept": "application/json, text/javascript, */*; q=0.01",
#         "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#         "X-Requested-With": "XMLHttpRequest",
#         "Host": "www.lagou.com",
#         "Connection":"keep-alive",
#         "Origin": "https://www.lagou.com",
#         "Upgrade-Insecure-Requests":"1",
#         "X-Anit-Forge-Code": "0",
#         "X-Anit-Forge-Token": "None",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "zh-CN,zh;q=0.8"
#         }
#     return headers
