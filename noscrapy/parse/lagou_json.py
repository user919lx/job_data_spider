import pandas as pd
import json
import os
kd = "数据工程"  # 搜索关键词
city = ""  # 城市
read_dir_path = "../temp/json/kd_"+kd
write_path = "../clean_data/lagou_json_kd_"+kd+".xls"


# ---------------- 读取，合并json数据到一个DataFrame里 ------------------------
df = pd.DataFrame()
i = 1
for parent,dirnames,filenames in os.walk(read_dir_path):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for filename in filenames:                        #输出文件信息
        json_path = os.path.join(parent,filename)
        with open(json_path, encoding='utf-8-sig') as f:
            r = json.load(f)
            jobs = r['content']['positionResult']['result']
            print(i)
            jdf = pd.DataFrame(jobs)
            df = pd.concat([df, jdf])
            i = i + 1
# --------------- 数据清洗 -------------------------------
# 行清理
# 以positionId为准，删去重复的职位
df.drop_duplicates(subset='positionId',inplace=True)
# 设置positionId为索引
df.set_index('positionId',inplace=True)

# 列清理
# 删去空的列
df.dropna(1, how='all',inplace=True)
# 删去不需要的列 (意义不明的信息和重复的信息）
drop_list = ['adWord', 'appShow', 'approve', 'companyFullName', 'companyLogo', 'deliver',
             'formatCreateTime', 'createTime', 'companyId', 'imState', 'lastLogin', 'pcShow', 'score', 'publisherId']
df.drop(drop_list, axis=1, inplace=True)


# 排序
sort_list = ['firstType', 'secondType', 'industryField', 'companySize', 'financeStage', 'companyShortName', 'district']
df.sort_values(sort_list, inplace=True, ascending=False)


df.to_excel(write_path)
