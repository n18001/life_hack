#!/usr/bin/python3


# UtaTenの歌詞ランキングTop30を取得する
import requests, bs4


# リクエストとスープ
def requesoup(url):
    return bs4.BeautifulSoup(requests.get(url).text, 'lxml')


# 歌詞ランキングを取ってくる
def songRank(page):
    elem_box = ['SongRank SongName SingerName']
    for elem in page.find_all('article', class_='lst_boxArea'):
        songRank = elem.find('span', class_='icoTxt_rank').string.strip()
        songName = elem.find('h3', class_='boxArea_ttl').string.strip()
        singerName = elem.find('p', class_='boxArea_artists').string.strip()
        elem_set = '{} {} {}'.format(songRank, songName, singerName)
        elem_box.append(elem_set)
    return elem_box


# 表示
def display(d):
    print(d)


# 実行
if __name__ == '__main__':
    url = 'https://utaten.com/lyricPvRanking/index'
    display('UtaTen歌詞ランキングTOP30!')
    for rank in songRank(requesoup(url)):
        display(rank)
