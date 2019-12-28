import requests
import re
import json
import csv
import codecs
import os
import time
i = 0
j = 0
name = []
date = []
score = []
title = []
link = []
CommentNumber = 0
MaxNumber = 0
Element = {}
Settings={}
Cookies={}
headers={}

class Douban(object):
    # 爬取豆瓣电影上海堡垒前六页最热门评论作者与影评信息
    PageNumber = 1  # 页数
    CommentNumber = 0  # 评论数量
    # 获取网站地址(url)

    def Tools(self):
        global Settings
        global Element
        self.Element = Element
        self.Settings=Settings
        # 获取header中的用户id、名字、时间、评分数据
        Element['Header'] = r'class="main-hd">(.+?)</header>'
        # 内层div匹配获取评论标题和链接数据
        Element['Div'] = r'class="main-bd">(.+?)</div>'
        # 获取标题
        Element['Title'] = r'>(.+?)<'
        # 获取连接
        Element['Link'] = r'href="https://movie.douban.com/review/(.+?)"'
        # 获取时间
        Element['Date'] = r'class="main-meta">(.+?)</span>'
        # 获取评分
        Element['Score'] = r'title="(.+?)"></span>'
        # 获取用户id
        Element['UserId'] = r'people/(.+?)/" class="avator"'


    def Cookies(self):
        Cookies['cookie']=r'bid=FZmG0u5Abw8; ll="118282"; viewed="1236999"; gr_user_id=1526a73a-7cc6-4114-a6b1-a8d69b6e0494; __gads=ID=fc185450298c53cd:T=1572835664:S=ALNI_MatI2WugL6h5XVCzaF0wWXUhpu08A; _vwo_uuid_v2=D0C575F726774B7270361EEC5647245D7|39072f99e5a4263161f482b9460ff9dd; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1574063579%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DO4awfBSluo534wW2qdt5qQkbIj9FcvAlWFD63MC5nKa%26wd%3D%26eqid%3Ddf5406ae000d664b000000065dd24dd5%22%5D; _pk_ses.100001.8cb4=*; _pk_id.100001.8cb4=b765489f3edb5f22.1569204015.5.1574063975.1571740613.; __utma=30149280.103470262.1569204016.1572835656.1574063976.6; __utmc=30149280; __utmz=30149280.1574063976.6.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=30149280.1.10.1574063976; dbcl2="196614158:aWAsmT2EKaE"'
        return Cookies
    def Headers(self):
        headers['User-Agent']=r'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
        return headers

    def GetPage(self, CommentNumber,headers,cookies):
        self.headers=headers
        self.cookies=cookies
        url = "https://movie.douban.com/subject/26581837/reviews?start=%d" % self.CommentNumber
        page=requests.get(url,cookies=cookies,headers=headers)
        return page.text

    # 获取最大页数
    def MaxPage(self, page):
        TotalPageNumber = r'<span class="count">(.+?)</span>'
        TotalPageNumber = re.findall(TotalPageNumber, page, re.S)
        MaxPageNumber = int(re.sub('\D', '', TotalPageNumber[0]))
        return MaxPageNumber
    # 获取各个信息所用正则表达式

    # 筛选内容
    def GetData(self, page, Div, Header):
        List = {}
        List['DivElement'] = re.findall(
            Div, page, re.S)  # 匹配div标签中的内容
        List['HeaderElement'] = re.findall(
            Header, page, re.S)  # 匹配header标签中的内容
        return List

    def GetUserName(self, Line, UserId, Date, Score, i):
        GetUserId = re.findall(UserId, Line, re.S)
        userid = GetUserId[0]
        # 先获取用户id
        # 再获取用户名字,发表时间,分数
        Name = r'href="https://www.douban.com/people/' +\
            userid+'/" class="name">(.+?)</a>'
        GetName = re.findall(Name, Line, re.S)
        name.insert(i, GetName[0])
        GetDate = re.findall(Date, Line, re.S)
        date.insert(i, GetDate[0][1])
        GetScore = re.findall(Score, Line, re.S)
        if GetScore:  # 判断是否有评分
            score.insert(i, GetScore[0][0])
        else:
            score.insert(i, " ")  # 无评分

    def GetTitle_N_Link(self, line, Title, Link, j):
        GetTitle = re.findall(Title, line, re.S)  # 获取评论标题
        title.insert(j, GetTitle[0])
        GetLink = re.findall(Link, line, re.S)  # 获取评论连接
        link.insert(j, GetLink[0])

    def init(self):
        global CommentNumber, MaxNumber
        cookies=Douban().Cookies()
        headers=Douban().Headers()
        Douban().Tools()
        Page = Douban().GetPage(CommentNumber,headers,cookies)
        MaxNumber = Douban().MaxPage(Page)
        for index in range(MaxNumber):  # 外循环 用于控制翻页
            Page = Douban().GetPage(CommentNumber,headers,cookies)
            List = Douban().GetData(Page,Element.get('Div'),Element.get('Header'))
            for Line in List['DivElement']:  # 获取div中数据
                global j
                Douban().GetTitle_N_Link(Line,Element.get('Title'),Element.get('Link'),j)
                j += 1
                time.sleep(30)
            for line in List['HeaderElement']:
                global i
                Douban().GetUserName(line,Element.get('UserId'),Element.get('Date'),Element.get('Score'),i)
                i += 1
                time.sleep(30)
            CommentNumber += 20


if __name__ == "__main__":
    Douban()
    Douban().init()
