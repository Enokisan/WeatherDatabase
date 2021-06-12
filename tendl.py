import urllib.request as req

def download():
    # URLや保存ファイル名を指定
    url = 'https://www.jma.go.jp/bosai/forecast/data/forecast/010000.json'
    filename = 'tenki.json'
    # ダウンロード
    req.urlretrieve(url, filename)
    print("[Weather Database] tenki.json has been downloaded!\n")