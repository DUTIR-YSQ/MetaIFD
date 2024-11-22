
import dashscope
dashscope.api_key="sk-aefc5f861ad54280865ec5d4f04ad62f"
import json

import time

# 读取JSON文件
file_path="kevin"
#file_path="bizzoni"
#file_path="Reimann"
#file_path="COTinverse_new"
#file_path="COTkatz_new"
#file_path="figqa_sentiment_sentiment"
#file_path="MUHCHgeneration"#2925
#file_path="judgement"#1116
#file_path="LCCen_new_fliter_new_new_new"#284975**
#file_path="LCCen_sentiment_sentiment_sentiment"#37151**
#file_path="MOH"#1602
#file_path="Trofi"#3736
#file_path="TSV"#421
#file_path="VUA_sentiment_sentiment"#181487**
#file_path="VUAtest"#22195**
start_time = time.time()
file_path="Completed/"+file_path
with open('Reimann.json', 'r', encoding='utf-8') as file:
    data_list = json.load(file)



for data in data_list:

    data['Metaphor_word_number'] =len(data['Metaphor_word'])

    with open('Reimann_sentiment.json', 'w', encoding='utf-8') as file:
        json.dump(data_list, file, ensure_ascii=False, indent=4)

with open('Reimann_sentiment.json', 'w', encoding='utf-8') as file:
    json.dump(data_list, file, ensure_ascii=False, indent=4)