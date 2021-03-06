import json
import weatherMethods as we
import tendl

def main():
    while True:
        with open('tenki.json', 'r', encoding="UTF-8") as f:
            data = json.load(f)
        query_num = int(input("[Weather Database] What do you want? type {0:quit, 1:pick up all, 2:select area, 3: download json}\n"))
        if query_num == 0:
            print("[Weather Database] End. Bye-bye!\n")
            break

        elif query_num == 1:
            print("[Weather Database] Pick up all.\n")
            which_data = int(input("[Weather Database] type {0:back, 1:weathers, 2:winds, 3:waves}\n"))
            if which_data == 0:
                print("[Weather Database] Back.\n")
                continue
            elif which_data == 1:
                we.weathers_all(data)
            elif which_data == 2:
                we.winds_all(data)
            elif which_data == 3:
                we.waves_all(data)
            else:
                print("[Weather Database] Query {} is not supported!\n".format(which_data))
                continue

        elif query_num == 2:
            area = input("[Weather Database] Select Area.\n")
            which_data = int(input("[Weather Database] type {0:back, 1:weathers, 2:winds, 3:waves, 4:weekly pops}\n"))
            if which_data == 0:
                print("[Weather Database] Back.\n")
                continue
            elif which_data == 1:
                we.weather_sel(data, area)
            elif which_data == 2:
                we.wind_sel(data, area)
            elif which_data == 3:
                we.wave_sel(data, area)
            elif which_data == 4:
                we.pops_weekly(data, area)
            else:
                print("[Weather Database] Query {} is not supported!\n".format(which_data))
                continue

        elif query_num == 3:
            tendl.download()

        else:
            print("[Weather Database] Query {} is not supported!\n".format(query_num))

if __name__ == "__main__":
    main()