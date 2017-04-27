import pandas as pd
import json

df = pd.DataFrame
for i in range(1, 21):
    json_filename = "job_lists/lagou_json_data_"+str(i)+".json"
    with open(json_filename, encoding='utf-8-sig') as f:
        r = json.load(f)
        jobs = r['content']['positionResult']['result']


        df.duplicated