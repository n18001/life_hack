#!/usr/bin/python3


# アニメを取ってくるだけ
import requests, json
from datetime import datetime


# URL
def getAnimeURL(year, cours):
    URL = 'http://api.moemoe.tokyo/anime/v1/master/{}/{}'.format(year, cours)
    return URL


# Jsonを読む
def readJson(url):
    r = requests.get(url)
    data = json.loads(r.text)
    return data


# アニメの名前を取得
def getAnimeName(data):
    anime_list = []
    for animest in range(len(data)):
        info = '・{}: {}'.format(data[animest]['title'], data[animest]['public_url'])
        anime_list.append(info)
    return anime_list


# アニメの名前を出力
def showAnimeName(anime_list):
    for name in anime_list:
        desplay(name)


# ディスプレイ
def desplay(d):
    print(d)


# 実行
if __name__ == '__main__':
    while True:
        try:
            year = int(input('年: '))
            cours = int(input('期(1~4): '))
            if not (2014 <= year <= int(datetime.now().strftime('%Y'))) or not (1 <= cours <= 4):
                desplay('Error')
                break
            else:
                showAnimeName(getAnimeName(readJson(getAnimeURL(year, cours))))
                break
        except ValueError:
            desplay('ERROR')
            break
