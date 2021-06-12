import json

def weathers_all(data_in):
    s = ""
    for area in data_in:
        name = area['name']
        s += "[ " + str(name) + " ]\n"
        for ts in area['srf']['timeSeries']:
            times = [n for n in ts['timeDefines']]
            if 'weathers' in ts['areas']:
                for i,v in enumerate(ts['areas']['weathers']):
                    s += str(times[i]) + " : " + v + "\n"
    print(s)

def winds_all(data_in):
    s = ""
    for area in data_in:
        name = area['name']
        s += "[ " + str(name) + " ]\n"
        for ts in area['srf']['timeSeries']:
            times = [n for n in ts['timeDefines']]
            if 'winds' in ts['areas']:
                for i,v in enumerate(ts['areas']['winds']):
                    s += str(times[i]) + " : " + v + "\n"
    print(s)

def waves_all(data_in):
    s = ""
    for area in data_in:
        name = area['name']
        s += "[ " + str(name) + " ]\n"
        for ts in area['srf']['timeSeries']:
            times = [n for n in ts['timeDefines']]
            if 'waves' in ts['areas']:
                for i,v in enumerate(ts['areas']['waves']):
                    s += str(times[i]) + " : " + v + "\n"
    print(s)

def weather_sel(data_in, area_name):
    s = ""
    for area in data_in:
        if area['name'] == area_name:
            s += "[ " + str(area_name) + " ]\n"
            for ts in area['srf']['timeSeries']:
                times = [n for n in ts['timeDefines']]
                if 'weathers' in ts['areas']:
                    for i,v in enumerate(ts['areas']['weathers']):
                        s += str(times[i]) + " : " + v + "\n"
    print(s)

def wind_sel(data_in, area_name):
    s = ""
    for area in data_in:
        if area['name'] == area_name:
            s += "[ " + str(area_name) + " ]\n"
            for ts in area['srf']['timeSeries']:
                times = [n for n in ts['timeDefines']]
                if 'winds' in ts['areas']:
                    for i,v in enumerate(ts['areas']['winds']):
                        s += str(times[i]) + " : " + v + "\n"
    print(s)

def wave_sel(data_in, area_name):
    s = ""
    for area in data_in:
        if area['name'] == area_name:
            s += "[ " + str(area_name) + " ]\n"
            for ts in area['srf']['timeSeries']:
                times = [n for n in ts['timeDefines']]
                if 'waves' in ts['areas']:
                    for i,v in enumerate(ts['areas']['waves']):
                        s += str(times[i]) + " : " + v + "\n"
    print(s)

"""
# デバッグ用
# ダウンロードしたファイルを開く
with open('tenki.json', 'r', encoding="UTF-8") as f:
  data = json.load(f)
# 読み出したデータを解析
weather_all(data)
"""
