import pandas as pd
import matplotlib.pyplot as plt
import re
# %matplotlib inline
# 中文字体显示
plt.rc('font', family='SimHei', size=13)

def translate_first_type(str):
    str = str.replace("\s", "")
    if str == "综合职能类":
        str = "职能"
    elif str == "金融类":
        str = "金融"
    elif str == "设计类":
        str = "设计"
    elif str == "市场/商务/销售类":
        str = "市场与销售"
    elif str == "产品/需求/项目类":
        str = "产品"
    elif str == "运营/编辑/客服":
        str = "运营"
    elif str == "开发/测试/运维类":
        str = "技术"
    return str

reg = re.compile(r'(\d+)[kK]-(\d+)[kK]')


def salary_to_minmax(str):
    m = reg.match(str)
    return pd.Series({'min_salary': int(m.group(1)), 'max_salary': int(m.group(2))})

df = pd.read_excel('noscrapy/job_data.xls', index_col=0)
df['firstType'] = df['firstType'].apply(translate_first_type)
minmax = df['salary'].apply(salary_to_minmax)
df.insert(5,'max_salary',minmax['max_salary'])
df.insert(5,'min_salary',minmax['min_salary'])
df.insert(5,'avg_salary',minmax.mean(axis=1))
df.drop('salary', axis=1, inplace=True)

sort_list = ['firstType', 'secondType', 'industryField', 'companySize', 'financeStage', 'companyShortName', 'district']
df.sort_values(sort_list, inplace=True, ascending=False)
df.to_excel('noscrapy/clean_jobs.xls')

ds = df.pivot_table(['avg_salary','min_salary'], rows=['firstType'], margins=True)
ds
# ds = df.groupby(['firstType']).describe()
# ds['avg_salary'].unstack().drop('count',axis=1).plot.bar()
# plt.show()