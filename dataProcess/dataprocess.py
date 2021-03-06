import json
import csv

path = './iron_ore.csv'
All_data = []
with open(path, encoding='utf8') as f:
    datas = csv.reader(f)
    next(datas)
    for data in datas:
        All_data.append({
            'Export': data[0], 'Ex_Pos': {'lon': float(data[1]), 'lat': float(data[2])},
            'Import': data[3], 'Im_Pos': {'lon': float(data[4]), 'lat': float(data[5])},
            'trade_num': int(data[6])
        })

with open('The Trade number.json', 'w', encoding='utf8') as f_object:
    json.dump(All_data, f_object, ensure_ascii=False)
