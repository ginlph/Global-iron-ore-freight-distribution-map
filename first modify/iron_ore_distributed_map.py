import json
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm
import cartopy.crs as ccrs
import numpy as np
import matplotlib as mpl
plt.rcParams['font.sans-serif'] =['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号

"""
one = {'Export': '澳大利亚', 'Ex_Pos': {'lon': 118.53, 'lat': -20.3}, 
       'Import': '中国', 'Im_Pos': {'lon': 118.5, 'lat': 38.9}, 'trade_num': 71463}
"""


with open('../dataProcess/The Trade number.json', encoding='utf8') as f:
    datas = json.load(f)

fig = plt.figure(figsize=(15, 8), dpi=150)
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([-180, 180, -90, 90])
ax.coastlines()
# ax.stock_img()


trade_num = [int(data['trade_num']) for data in datas]
trade_max = max(trade_num)
trade_min = min(trade_num)
normalize = mcolors.Normalize(vmin=trade_min, vmax=trade_max)
colormap = cm.RdYlBu


for data in datas:
    trade = normalize(int(data['trade_num']))
    if int(data['trade_num']) < 10:
        ax.plot([float(data['Ex_Pos']['lon']), float(data['Im_Pos']['lon'])],
            [float(data['Ex_Pos']['lat']), float(data['Im_Pos']['lat'])],
            color=colormap(trade), linewidth=trade+0.5, alpha=trade+0.1)
    elif 10 <= int(data['trade_num']) < 100:
        ax.plot([float(data['Ex_Pos']['lon']), float(data['Im_Pos']['lon'])],
                [float(data['Ex_Pos']['lat']), float(data['Im_Pos']['lat'])],
                color=colormap(trade), linewidth=trade+0.5, alpha=trade+0.1)
    elif 100 <= int(data['trade_num']) < 1000:
        ax.plot([float(data['Ex_Pos']['lon']), float(data['Im_Pos']['lon'])],
                [float(data['Ex_Pos']['lat']), float(data['Im_Pos']['lat'])],
                color=colormap(trade), linewidth=trade+0.5, alpha=trade+0.1)
    elif 1000 <= int(data['trade_num']) < 2000:
        ax.plot([float(data['Ex_Pos']['lon']), float(data['Im_Pos']['lon'])],
                [float(data['Ex_Pos']['lat']), float(data['Im_Pos']['lat'])],
                color=colormap(trade), linewidth=trade+0.5, alpha=trade+0.1)
    elif 2000 <= int(data['trade_num']) < 3000:
        ax.plot([float(data['Ex_Pos']['lon']), float(data['Im_Pos']['lon'])],
                [float(data['Ex_Pos']['lat']), float(data['Im_Pos']['lat'])],
                color=colormap(trade), linewidth=1.5, alpha=trade+0.3)
        if data['Export'] == "马来西亚":
            ax.text(float(data['Ex_Pos']['lon']), float(data['Ex_Pos']['lat']),
                    "{}".format(data['Export']), fontsize=8)

    elif 3000 <= int(data['trade_num']) < 5000:
        ax.plot([float(data['Ex_Pos']['lon']), float(data['Im_Pos']['lon'])],
                [float(data['Ex_Pos']['lat']), float(data['Im_Pos']['lat'])],
                color=colormap(trade), linewidth=1.5, alpha=trade + 0.3)

    elif 5000 <= int(data['trade_num']) < 8000:
        ax.plot([float(data['Ex_Pos']['lon']), float(data['Im_Pos']['lon'])],
                [float(data['Ex_Pos']['lat']), float(data['Im_Pos']['lat'])],
                color=colormap(trade), linewidth=1.5, alpha=trade+0.3)
        if data['Import'] == "日本":
            ax.text(float(data['Im_Pos']['lon']), float(data['Im_Pos']['lat']) - 5,
                    "{}".format(data['Import']), fontsize=12)
        if data['Import'] == "韩国":
            ax.text(float(data['Im_Pos']['lon']), float(data['Im_Pos']['lat']),
                    "{}".format(data['Import']), fontsize=12)

    else:
        ax.plot([float(data['Ex_Pos']['lon']), float(data['Im_Pos']['lon'])],
                [float(data['Ex_Pos']['lat']), float(data['Im_Pos']['lat'])],
                color=colormap(trade), linewidth=3, alpha=trade)
        ax.text(float(data['Ex_Pos']['lon'])-10, float(data['Ex_Pos']['lat'])-6,
                "{}".format(data['Export']), fontsize=20)
        ax.text(float(data['Im_Pos']['lon'])-10, float(data['Im_Pos']['lat'])-6,
                "{}".format(data['Import']), fontsize=20)
# setup the colorbar

cax = fig.add_axes([0.93, 0.2, 0.02, 0.6])
cb = mpl.colorbar.ColorbarBase(cax, cmap=colormap, norm=normalize)
plt.savefig("Global iron ore freight distribution map.png")
plt.show()
