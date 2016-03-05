from bs4 import BeautifulSoup
import requests
import time

def pages_details(url,data=None):
    header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
    wb_data = requests.get(url,header)
    time.sleep(4)
    #分析抓取地址
    Soup = BeautifulSoup(wb_data.text,'lxml')
    #av标题
    titles = Soup.select('body > div.container > h3')
    #av封面图
    images = Soup.select('body > div.container > div.row.movie > div.col-md-9.screencap > a > img')
    #av番号
    movie_ids = Soup.select('body > div.container > div.row.movie > div.col-md-3.info > p:nth-of-type(1) > span:nth-of-type(2)')
    #av的系列
    series = Soup.select('body > div.container > div.row.movie > div.col-md-3.info > p:nth-of-type(10) > a')
    #av类别 - 多内容
    genres = Soup.select('body > div.container > div.row.movie > div.col-md-3.info > p > span > a')
    #av演员 - 多内容
    players = Soup.select('#avatar-waterfall > a > span')
    #av播放截图 - 多内容
    simples = Soup.select('#sample-waterfall > a > div > img')

    #print("设定完成,构建列表")

    #抓取并写入字典
    Series = []
    Genre = []
    Player =[]
    Simple =[]
    for serie in series:
        Series.append(serie.get_text())
    for genre in genres:
        Genre.append(genre.get_text())
    for player in players:
        Player.append(player.get_text())
    for simple in simples:
        Simple.append(simple.get('src'))
    if len(Series)==0:
        Series.append('None')

    if len(Genre)==0:
        Genre.append('None')

    if len(Player)==0:
        Player.append('None')

    if len(Simple)==0:
        Simple.append('None')

    print("列表构建完成,开始写入字典")
    if data == None:
        for title,image,movie_id in zip(titles,images,movie_ids):
                data = {
                    'av标题':title.get_text(),
                    'av封面图':image.get('src'),
                    'av番号':movie_id.get_text(),
                    'av系列':Series,
                    'av类别':Genre,
                    'av演员':Player,
                    'av播放截图':Simple
                }
        print(data)

