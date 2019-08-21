import urllib.request  
import re 
import json
import csv
import codecs
import os
import time

i=0
j=0
name=[]
time_1=[]
score=[]
title=[]
link=[]

#爬取豆瓣电影上海堡垒前六页最热门评论作者与影评信息
PageNumber=1#页数
CommentNumber=0 #评论数量
#获取网站地址(url)
url="https://movie.douban.com/subject/26581837/reviews"
page=urllib.request.urlopen(url).read()
page=page.decode('utf8')

#获取最大页数
TotalPageNumber=r'<span class="count">(.+?)</span>'
TotalPageNumber=re.findall(TotalPageNumber,page,re.S)
MaxPageNumber=int(re.sub('\D','',TotalPageNumber[0]))
#获取各个信息所用正则表达式
Count1=r'<header class="main-hd">(.+?)</header>' #获取header中的用户id、名字、时间、评分数据
Count=r'<div class="main-bd">(.+?)</div>' # 内层div匹配获取评论标题和链接数据
Title=r'<a href="https://movie.douban.com/review/(.+?)/">(.+?)</a>' #获取标题和链接
Time=r'<span content="(.+?)" class="main-meta">(.+?)</span>'# 获取时间 
Score=r'<span class="allstar(.+?) main-title-rating" title="(.+?)"></span>' # 获取评分
UserId=r'<a href="https://www.douban.com/people/(.+?)/" class="avator">' #获取用户id

for index in range(MaxPageNumber): #外循环 用于控制翻页

    #翻页
    url="https://movie.douban.com/subject/26581837/reviews?start=%d"%CommentNumber
    if CommentNumber>=20:
        page=urllib.request.urlopen(url).read()
        page=page.decode('utf8','ignore')

    #筛选内容
    HtmlList=re.findall(Count,page,re.S) #匹配header标签中的内容
    HtmlList1=re.findall(Count1,page,re.S)#匹配div标签中的内容

    for line1 in HtmlList1: #获取用户id等数据
        GetUserId=re.findall(UserId,line1,re.S)
        userid=GetUserId[0]
        #先获取用户id
        #再获取用户名字,发表时间,分数
        Name='<a href="https://www.douban.com/people/'+userid+'/" class="name">(.+?)</a>'
        GetName=re.findall(Name,line1,re.S)
        name.insert(i,GetName[0])
        GetTime=re.findall(Time,line1,re.S)
        time_1.insert(i,GetTime[0][1])
        GetScore=re.findall(Score,line1,re.S)
        if GetScore: #判断是否有评分
            score.insert(i,GetScore[0][0])
        else:
            score.insert(i,0) #无评分
        i+=1
        print("第%d次"%i)
    #获取div中数据
    for line in HtmlList:
        Html_link=re.findall(Title,line,re.S)  #获取评论标题和链接
        title.insert(i,Html_link[0][1])
        link.insert(i,Html_link[0][0])
        CommentNumber+=1 #翻页
        j+=1
    #打印出该页最后一位作者的信息
  
    PageNumber+=1 #记录页数
    time.sleep(30)
    if i==MaxPageNumber:
        break

with open('C:\\Users\\admin\\Desktop\\data.csv','w',newline='',encoding='utf_8_sig') as f:
    writer = csv.writer(f)
    writer.writerow(('名字', '发表时间', '分数', '标题','连接'))
    for Num in range(CommentNumber):
        writer.writerow((name[Num],time_1[Num],score[Num],title[Num],"https://movie.douban.com/review/"+link[Num]))
        print("第"+i+"次写入")
f.close()
print("写入完毕")