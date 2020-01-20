import requests
import re
import json
import csv
import codecs
import os
import time
import selenium


def LoginInfo():
    info={}
    info={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    "Cookie":"bid=FZmG0u5Abw8; ll=\"118282\"; __yadk_uid=OfIOWagQWjLH65oCCYSQQMFuQASdsAOg; trc_cookie_storage=taboola%2520global%253Auser-id%3De70233ca-91bb-46a1-83b0-98daede6eaab-tuct467d03c; viewed=\"1236999\"; gr_user_id=1526a73a-7cc6-4114-a6b1-a8d69b6e0494; __gads=ID=fc185450298c53cd:T=1572835664:S=ALNI_MatI2WugL6h5XVCzaF0wWXUhpu08A; _vwo_uuid_v2=D0C575F726774B7270361EEC5647245D7|39072f99e5a4263161f482b9460ff9dd; __utmv=30149280.19661; __utma=30149280.103470262.1569204016.1578472587.1578553193.8; __utmz=30149280.1578553193.8.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=30149280; _ga=GA1.2.103470262.1569204016; _gid=GA1.2.213519578.1578553656; push_noty_num=0; push_doumail_num=0; __utma=223695111.377708448.1571729567.1571738965.1578555172.3; __utmc=223695111; __utmz=223695111.1578555172.3.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1578562573%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; _pk_id.100001.4cf6=0cfa5b9018395735.1571729567.4.1578562574.1578555382.; dbcl2=\"196614158\:w4rPu6BYHfc"
    }
    return info
def Login():
    info={}
    info=LoginInfo()
    headers=info["User-Agent"]
    cookies=info["Cookie"]
    doubanUrl="https://search.douban.com/movie/subject_search"
    search_text=input("请输入你要搜索的电影:")
    searchPage=requests.get(url=doubanUrl,headers=headers,cookies=cookies,params=search_text)
    return searchPage.text
def getmovieId(searchPage):
    root="<div id=\"root\" class=\"root\">(.+?)</div>"
    time.sleep(3)
    root=re.findall(root,searchPage,re.S)
    details=r"<div class=\"detail\">(.+?)</div>"
    details=re.findall(details,root,re.S)

def init():
    searchPage=Login()
    getmovieId(searchPage)
if __name__=="__main__":
    init()




