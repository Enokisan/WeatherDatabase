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

def pops_weekly(data_in, area_name):  # with reliability
    s = ""
    for area in data_in:
        if area['name'] == area_name:
            s += "[ " + str(area_name) + " ]\n"
            for ts in area['week']['timeSeries']:
                times = [n for n in ts['timeDefines']]
                if 'pops' in ts['areas']:
                    for i,v in enumerate(ts['areas']['pops']):
                        s += str(times[i]) + " : " + v + "\n"
    print(s)
"""
def temps_weekly(data_in, area_name):  # tempsMin and tempsMax
    s = ""
    for area in data_in:
        if area['name'] == area_name:
            s += "[ " + str(area_name) + " ]\n"
            for ts in area['week']['timeSeries']:
                times = [n for n in ts['timeDefines']]
                tempsMins = [tmin for tmin in ts['areas']['tempsMin']]
                if 'tempsMax' in ts['areas']:
                    for i,v in enumerate(ts['areas']['tempsMax']):
                        s += str(times[i]) + " :\n" + "Min: " + str(tempsMins[i]) + ",Max: " + v + "\n"
    print(s)
"""

"""
# ???????????????
# ?????????????????????????????????????????????
with open('tenki.json', 'r', encoding="UTF-8") as f:
  data = json.load(f)
# ?????????????????????????????????
weather_all(data)
"""
