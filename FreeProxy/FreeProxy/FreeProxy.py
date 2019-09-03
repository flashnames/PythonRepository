import re
import requests
import csv
More=r'<tr>(.+?)</tr>'
Data=r'<td>(.+?)</td>'
data=[]
port=[]
type=[]
connect=[]
city=[]
time=[]
j=0
i=0
class Proxy:
    def cookies():
        cookies={'cookie':'pgv_pvi=6406694912; pgv_si=s1000139776'}
        return cookies
    def headers():
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
        return headers
    def Url(headers,cookies):
        url=requests.get("https://lab.crossincode.com/Proxy/",headers=headers,cookies=cookies)
        return url.text

    def Page(url):
        page=r'<div class="center-block root-index-block">(.+?)</div>'
        page=re.findall(page,url,re.S)
        return page
    def GetIp(page):
        global j
        global i
        for Html in page:
            GetMore=re.findall(More,Html,re.S)
            for Line in GetMore:
               GetData=re.findall(Data,Line,re.S)
               if GetData:
                   data.insert(j,GetData[0])
                   port.insert(j,GetData[1])
                   type.insert(j,GetData[2])
                   connect.insert(j,GetData[3])
                   city.insert(j,GetData[4])
                   time.insert(j,GetData[5])
    def WriterFile():
            with open('C:\\Users\\admin\\Desktop\\PythonCode\\FreeProxy\\FreeProxy\\Data.csv','w',newline='',encoding='utf_8_sig') as f:
                writer = csv.writer(f)
                writer.writerow(('Ip地址', '端口', '连接类型','连接协议','城市','时间'))
                for Num in range(j):
                    writer.writerow((data[Num],port[Num],type[Num],connect[Num],city[Num],time[Num]))
                    print("第%d次写入"%Num)
                f.close()
                print("写入完毕")
    def init():
        cookies=Proxy.cookies()
        headers=Proxy.headers()
        url=Proxy.Url(headers,cookies)
        page=Proxy.Page(url)
        Proxy.GetIp(page)
        Proxy.WriterFile()

if __name__=="__main__":
    Proxy()
    Proxy.init()