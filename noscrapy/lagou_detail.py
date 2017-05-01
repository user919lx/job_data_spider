import json
import requests
import codecs
from bs4 import BeautifulSoup
import time

def save_html(text, index):
    filename = "job_detail/lagou_" + str(index) + ".html"
    file = codecs.open(filename, "w", "utf-8-sig")
    file.write(text)
    file.close()



ids_set = set()
for i in range(1, 21):
    json_filename = "job_lists/lagou_json_data_"+str(i)+".json"
    with open(json_filename, encoding='utf-8-sig') as f:
        r = json.load(f)
        jobs = r['content']['positionResult']['result']
        position_ids = set([job['positionId'] for job in jobs])
        ids_set = ids_set | position_ids

s = requests.Session()
failure_limits = 100
failure_count = 0
while len(ids_set) > 0 and failure_count<failure_limits:
    position_id = ids_set.pop()
    url = "https://www.lagou.com/jobs/"+str(position_id)+".html"
    resp = s.get(url)
    try:
        bs_obj = BeautifulSoup(resp.text, "html5lib")
        desc = bs_obj.find("dd", {'class': 'job_bt'})
        desc_lists = [p.text for p in desc.div.findAll("p")]
        desc_str = '\n'.join(desc_lists)
        address = bs_obj.find("input", {'name': "positionAddress"})['value']
        print(position_id, address, len(ids_set), failure_count)
        save_html(resp.text, position_id)

    except AttributeError:
        print("error: id = " + str(position_id))
        ids_set.add(position_id)
        failure_count = failure_count + 1
        time.sleep(60)

print(ids_set)
s.close()
