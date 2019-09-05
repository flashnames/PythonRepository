import re
import requests
import csv
import time
More=r'<tr class="odd">(.+?)</tr>'
Data=r'<td>(.+?)</td>'
data=[]
port=[]
survivaltime=[]
connect=[]
city=[]
checktime=[]
j=0
i=0
class Proxy:
    def cookies():
        cookies={'cookie':'td_cookie=1905952385; _free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTRiOWQ3Njk1ZjdjMmI2MWNkODUzZTU0ZDRiMmY2NWMyBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMVdMS0I2d21kWmVMbEYxTnhIdlZOS2RkUktUajIyZGJ5SUw4RU5LdDVOaEk9BjsARg%3D%3D--0fe2aba896c2046432c2d8aaf721483cc8d5e389; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1565598137,1567647843; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1567647843'}
        return cookies
    def headers():
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
        return headers
    def Url(headers,cookies):
        url=requests.get("https://www.xicidaili.com/",headers=headers,cookies=cookies)
        return url.text

    def Page(url):
        page=r'<table id="ip_list">(.+?)</table>'
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
                   city.insert(j,GetData[2])
                   connect.insert(j,GetData[3])
                   survivaltime.insert(j,GetData[4])
                   checktime.insert(j,GetData[5])
                   time.sleep(45)
                   j+=1
                   print("第%d次"%j)
    def WriterFile():
            with open('C:\\Users\\admin\\Desktop\\PythonCode\\FreeProxy\\FreeProxy\\Data.csv','w',newline='',encoding='utf_8_sig') as f:
                writer = csv.writer(f)
                writer.writerow(('Ip地址', '端口', '城市','连接协议','存活时间','检查时间'))
                for Num in range(j):
                    writer.writerow((data[Num],port[Num],city[Num],connect[Num],survivaltime[Num],checktime[Num]))
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
