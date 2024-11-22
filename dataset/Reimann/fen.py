import json
import math

# 读取JSON文件
file_path = 'Reimann_sentiment'
with open(file_path + '.json', 'r', encoding='utf-8') as file:
    data_list = json.load(file)

# 计算每个部分的大小
total_len = len(data_list)
test_size = math.floor(total_len * 0.1)
train_size = math.floor(total_len * 0.8)
val_size = total_len - train_size - test_size  # 确保总数相加为原列表大小# 按照比例划分数据
test_data = data_list[:test_size]
train_data = data_list[test_size:test_size + train_size]
val_data = data_list[test_size + train_size:]
with open(file_path + '_train.json', 'w', encoding='utf-8') as file:
    json.dump(train_data, file, ensure_ascii=False, indent=4)

with open(file_path + '_val.json', 'w', encoding='utf-8') as file:
    json.dump(val_data, file, ensure_ascii=False, indent=4)

with open(file_path + '_test.json', 'w', encoding='utf-8') as file:
    json.dump(test_data, file, ensure_ascii=False, indent=4)

print("数据已成功按8:1:1比例划分，并保存为三个文件。")