import requests
from bs4 import BeautifulSoup
s = requests.Session()
position_id = 1301956
# print(position_id)
url = "https://www.lagou.com/jobs/"+str(position_id)+".html"
resp = s.get(url)
print(position_id,resp.headers,resp.content,resp.status_code,resp.is_redirect,sep="\n")
try:
    bs_obj = BeautifulSoup(resp.text, "html5lib")
    desc = bs_obj.find("dd", {'class': 'job_bt'})
    desc_lists = [p.text for p in desc.div.findAll("p")]
    desc_str = '\n'.join(desc_lists)
    address = bs_obj.find("input", {'name': "positionAddress"})['value']
    print(desc_str,address,sep='\n')
    # save_html(resp.text, position_id)
    # success_count = success_count + 1
except AttributeError:
    print("error: id = " + str(position_id))
    # failed_ids.append(position_id)

s.close()