#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lph time:2019/3/30
import json
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib.colors as mcolors

plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号

with open("../dataProcess/The Trade number.json", encoding='utf8') as f:
    datas = json.load(f)

fig = plt.figure(figsize=(15, 8), dpi=150)
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([-180, 180, -90, 90])

trade_num = [data['trade_num'] for data in datas]
trade_max = max(trade_num)
trade_min = min(trade_num)
normalize = mcolors.Normalize(vmin=trade_min, vmax=trade_max)
# print(normalize(trade_num))

for data in datas:
    if 0 < data['trade_num'] < 100:
        ax.plot([data['Ex_Pos']['lon'], data['Im_Pos']['lon']], [data['Ex_Pos']['lat'], data['Im_Pos']['lat']],
                color='black', linewidth=normalize(data['trade_num'])+.5, alpha=0.1)
    elif 100 <= data['trade_num'] < 1000:
        ax.plot([data['Ex_Pos']['lon'], data['Im_Pos']['lon']], [data['Ex_Pos']['lat'], data['Im_Pos']['lat']],
                color='black', linewidth=normalize(data['trade_num'])+.5, alpha=0.15)
    elif 1000 <= data['trade_num'] < 2000:
        ax.plot([data['Ex_Pos']['lon'], data['Im_Pos']['lon']], [data['Ex_Pos']['lat'], data['Im_Pos']['lat']],
                color='black', linewidth=normalize(data['trade_num'])+0.5, alpha=0.2)
    elif 2000 <= data['trade_num'] < 3000:
        ax.plot([data['Ex_Pos']['lon'], data['Im_Pos']['lon']], [data['Ex_Pos']['lat'], data['Im_Pos']['lat']],
                color='black', linewidth=normalize(data['trade_num'])+0.8, alpha=0.45)
    elif 3000 <= data['trade_num'] < 5000:
        ax.plot([data['Ex_Pos']['lon'], data['Im_Pos']['lon']], [data['Ex_Pos']['lat'], data['Im_Pos']['lat']],
                color='black', linewidth=normalize(data['trade_num'])+1, alpha=0.5)
        ax.text(float(data['Ex_Pos']['lon']) - 10, float(data['Ex_Pos']['lat']) - 6,
                "{}".format(data['Export']), fontsize=10)
    elif 5000 <= data['trade_num'] < 8000:
        ax.plot([data['Ex_Pos']['lon'], data['Im_Pos']['lon']], [data['Ex_Pos']['lat'], data['Im_Pos']['lat']],
                color='black', linewidth=normalize(data['trade_num'])+1.3, alpha=0.6)
        if data['Import'] == "日本":
            ax.text(float(data['Im_Pos']['lon']), float(data['Im_Pos']['lat']) - 5,
                    "{}".format(data['Import']), fontsize=12)
        if data['Import'] == "韩国":
            ax.text(float(data['Im_Pos']['lon']), float(data['Im_Pos']['lat']),
                    "{}".format(data['Import']), fontsize=11)
    elif 8000 <= data['trade_num'] < 30000:
        ax.plot([data['Ex_Pos']['lon'], data['Im_Pos']['lon']], [data['Ex_Pos']['lat'], data['Im_Pos']['lat']],
                color='black', linewidth=normalize(data['trade_num'])+1.4, alpha=0.8)
        ax.text(float(data['Ex_Pos']['lon']) - 10, float(data['Ex_Pos']['lat']) - 6,
                "{}".format(data['Export']), fontsize=14)
    else:
        ax.plot([data['Ex_Pos']['lon'], data['Im_Pos']['lon']], [data['Ex_Pos']['lat'], data['Im_Pos']['lat']],
                color='black', linewidth=normalize(data['trade_num'])+2.5, alpha=normalize(data['trade_num']))
        ax.text(float(data['Ex_Pos']['lon']) - 10, float(data['Ex_Pos']['lat']) - 6,
                "{}".format(data['Export']), fontsize=16)
        ax.text(float(data['Im_Pos']['lon']) - 10, float(data['Im_Pos']['lat']) + 4,
                "{}".format(data['Import']), fontsize=20)




plt.savefig('./second iron.png')
plt.show()