import pandas as pd
import json
from bs4 import BeautifulSoup
import requests


df = pd.DataFrame()
# ---------------- 读取，合并json数据 ------------------------
# files = ['positionId','positionName','companyShortName']
for i in range(1, 21):
    json_filename = "job_lists/lagou_json_data_" + str(i) + ".json"
    with open(json_filename, encoding='utf-8-sig') as f:
        r = json.load(f)
        jobs = r['content']['positionResult']['result']
        jdf = pd.DataFrame(jobs)
        df = pd.concat([df, jdf])


# --------------- 数据清洗 -------------------------------
# 行清理
# 以positionId为准，删去重复的职位
df.drop_duplicates(subset='positionId',inplace=True)
# 去掉要求硕士/博士学历的
df = df[df.education.apply(lambda x: x != "硕士" and x != "博士")]
# 只看全职岗
df = df[df.jobNature == '全职']
# print(df.positionLables.apply(lambda x: str(x).find('实习') == -1))
df = df[df.positionLables.apply(lambda x: str(x).find('实习') == -1)]

# 设置positionId为索引
df.set_index('positionId',inplace=True)

# 因为可以在写入excel时决定写入哪些列，所以无需列清理
# 列清理
# 删去空的列
# df.dropna(1, how='all',inplace=True)
# 删去不需要的列 (意义不明的信息和重复的信息）
# drop_list = ['adWord', 'appShow', 'approve', 'companyFullName', 'companyLogo', 'deliver', 'city',
#              'formatCreateTime', 'createTime', 'companyId', 'imState', 'lastLogin', 'pcShow', 'score', 'publisherId']
# df.drop(drop_list, axis=1, inplace=True)

# 排序
sort_list = [ 'firstType', 'secondType', 'industryField', 'companySize', 'financeStage', 'companyShortName', 'district']
df.sort_values(sort_list, inplace=True, ascending=False)

# # ----------------- 根据positionId读取下载下来的网页，解析其中的关键内容（岗位描述，具体工作地址） ------------------------


def geocode(address):
    parameters = {'address': address, 'key': 'a3690d0216a44cf02c9fe55fe24a923a', 'city': "深圳"}
    base = 'http://restapi.amap.com/v3/geocode/geo'
    response = requests.get(base, parameters)
    resp = response.json()
    if resp['status'] == '1':
        try:
            formatted_address = resp['geocodes'][0]['formatted_address'],
            location = resp['geocodes'][0]['location']
        except IndexError:
            formatted_address = address
            location = ''
    else:
        formatted_address = address
        location = ''
    return {
        'formatted_address': formatted_address,
        'location': location
    }

detail_lists = []
for id in df.index:
    filename = "job_detail/lagou_"+str(id)+".html"
    with open(filename, encoding='utf-8-sig') as f:
        bs_obj = BeautifulSoup(f.read(), "html5lib")
        desc = bs_obj.find("dd", {'class': 'job_bt'})
        desc_lists = [p.text for p in desc.div.findAll("p")]
        desc_str = '\n'.join(desc_lists)
        address = bs_obj.find("input", {'name': "positionAddress"})['value']
        print(id,address)
        # geo = geocode(address)
        detail = (id, [address, desc_str])
        detail_lists.append(detail)

desc_df = pd.DataFrame.from_items(detail_lists, orient='index', columns=['address', 'desc'])
df = pd.merge(desc_df, df, how='outer', left_index=True, right_index=True)

print(df.shape)
# 保存为excel文件
columns_order = ['firstType', 'secondType', 'industryField', 'positionName', 'salary', 'companyShortName',
                 'positionLables', 'positionAdvantage', 'companySize', 'financeStage', 'companyLabelList',
                 'district', 'businessZones', 'workYear', 'education','address', 'desc']
df.to_excel("job_data.xls", columns=columns_order)
