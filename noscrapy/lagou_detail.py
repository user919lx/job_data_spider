import json
import requests
import codecs


def save_html(text,index):
    filename = "job_detail/lagou_" + str(index) + ".html"
    file = codecs.open(filename, "w", "utf-8-sig")
    file.write(text)
    file.close()


s = requests.Session()
count = 0
for i in range(2, 21):
    json_filename = "job_lists/lagou_json_data_"+str(i)+".json"
    with open(json_filename,encoding='utf-8-sig') as f:
        r = json.load(f)
        jobs = r['content']['positionResult']['result']
        for job in jobs:
            position_id = job['positionId']
            # print(position_id)
            url = "https://www.lagou.com/jobs/"+str(position_id)+".html"
            resp = s.get(url)
            save_html(resp.text, position_id)
            count = count + 1
            print(count)

s.close()
