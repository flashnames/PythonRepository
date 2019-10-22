import urllib.request
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


class Douban(object):
    # 爬取豆瓣电影上海堡垒前六页最热门评论作者与影评信息
    PageNumber = 1  # 页数
    CommentNumber = 0  # 评论数量
    # 获取网站地址(url)

    def Tools(self):
        global Element
        self.Element=Element
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

    def GetPage(self, CommentNumber):
        url = "https://movie.douban.com/subject/26581837/reviews?start=%d" % self.CommentNumber
        page = urllib.request.urlopen(url).read()
        page = page.decode('utf8')
        return page

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
            Header,page, re.S)  # 匹配header标签中的内容
        return List

    def GetUserName(self, Line, UserId, Date, Score, i):
        GetUserId = re.findall(UserId,Line, re.S)
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
        Douban().Tools()
        Page = Douban().GetPage(CommentNumber)
        MaxNumber = Douban().MaxPage(Page)
        for index in range(MaxNumber):  # 外循环 用于控制翻页
            Page = Douban().GetPage(CommentNumber)
            List = Douban().GetData(
                Page,
                Element.get('Div'),
                Element.get('Header')
            )
            for Line in List['DivElement']:  # 获取div中数据
                global j
                Douban().GetTitle_N_Link(
                    Line,
                    Element.get('Title'),
                    Element.get('Link'),
                    j
                )
                j += 1
                time.sleep(30)
            for line in List['HeaderElement']:
                global i
                Douban().GetUserName(
                    line,
                    Element.get('UserId'),
                    Element.get('Date'),
                    Element.get('Score'),
                    i
                )
                i += 1
                time.sleep(30)
            CommentNumber += 20


if __name__ == "__main__":
    Douban()
    Douban().init()
