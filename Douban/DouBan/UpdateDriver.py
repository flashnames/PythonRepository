import requests
import re

def googledriverUrl():
    Url="http://chromedriver.storage.googleapis.com/index.html"
    VersionPage=requests.get(Url)
    return VersionPage.text
def findVersion(VersionPage):
    body=r'<body>(.+?)</body>'
    body=re.findall(body,VersionPage,re.S)
    table=r'>(.+?)</table>'
    table=re.findall(table,body,re.S)
    tbody=r'>(.+?)</tbody>'
    tbody=re.findall(tbody,table,re.S)
    trs=r">(.+?)</tr>"
    trs=re.findall(trs,tbody,re.S)
    return trs


def init():
    VersionPage=googledriverUrl()
    findVersion(VersionPage)
if __name__=="__main__":
    print(init())