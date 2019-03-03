#!/usr/bin/python3


# アマゾン書籍売り上げランキングの取得
import requests, bs4


# リクエストとスープ
def requesoup(url):
    return bs4.BeautifulSoup(requests.get(url).text, 'lxml')


# 5ページ分のURL取得
def getAllURL(url):
    url_list = []
    for page in url.find_all('li', class_='zg_page'):
        pages = page.find('a').get('href')
        url_list.append(pages)
    return url_list


# 情報を取る
def getInfo(pages, p_number):
    info_list = []
    for elem in requesoup(pages[p_number]).find_all('div', class_='zg_itemRow'):
        rank = elem.find('span', class_='zg_rankNumber').string.strip()
        name = elem.find_all('div', class_='p13n-sc-truncate')[0].string.strip()
        price = elem.find('span', class_='p13n-sc-price').string.strip()
        info_list.append('{} {} {}'.format(rank, price, name))
    return info_list


# 情報の表示
def showInfo(info):
    for number in range(len(info)):
        display(info[number])


# 表示
def display(d):
    print(d)


# 実行
if __name__ == '__main__':
    url = 'https://www.amazon.co.jp/gp/bestsellers/books/2501045051/ref=zg_bs_2501045051_pg_1?ie=UTF8&pg=1'
    pages = getAllURL(requesoup(url))
    number = 0
    showInfo(getInfo(pages, number))
    answer = ['no', 'No', 'nO', 'NO', 'の']
    while True:
        if number >= 4:
            display('以上')
            break
        else:
            pass
        display('続きを表示しますか?')
        user = input('yes or no: ')
        if (user in answer):
            break
        else:
            number += 1
            showInfo(getInfo(pages, number))
            continue
