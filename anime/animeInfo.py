#!/usr/bin/python3


# アニメを取ってくる
# アニメの情報を載せる
# 時々エラーでるよ
import requests, json
from datetime import datetime


# api
def getAnimeURL(year, cours):
    return 'http://api.moemoe.tokyo/anime/v1/master/{}/{}'.format(year, cours)


# Jsonを読む
def readJson(url):
    r = requests.get(url)
    data = json.loads(r.text)
    return data


# アニメのURLを取得
def getAnimeName(data):
    anime_list = []
    for animest in range(len(data)):
        anime_list.append(data[animest]['public_url'])
    return anime_list


# アニメのURLから詳細を取るためのapi
def getAnimeInfoURL(anime_list):
    api_url = 'http://api.hitonobetsu.com/ogp/analysis?url={}'
    anime_info_URL = []
    for url in anime_list:
        anime_info_URL.append(api_url.format(url))
    return anime_info_URL


# アニメの詳細を取ってくる
def getAnimeInfo(anime_list):
    anime_info = []
    for page in anime_list:
        data = readJson(page)
        if data == []:
            continue
        info = {
            "name": data['title'],
            "description": data['description']
        }
        anime_info.append(info)
    return anime_info


# 形
def printAnimeInfo(anime_info):
    for page in range(len(anime_info)):
        msg = '''
        ~~~{}~~~
・{}'''
        desplay(msg.format(anime_info[page]['name'], anime_info[page]['description']))


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
                printAnimeInfo(getAnimeInfo(getAnimeInfoURL(getAnimeName(readJson(getAnimeURL(year, cours))))))
                break
        except ValueError:
            desplay('ERROR')
            break
