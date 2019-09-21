import re
import requests
import csv

class Proxy:
    def Read():
        with open('C:\\Users\\admin\\Desktop\\PythonCode\\FreeProxy\\FreeProxy\\Data.csv','r+',newline='',encoding='utf_8_sig') as f:
            reader=csv.reader(f)
            for i in reader:
                print(i[0])
class Tools(object):
    def headers():
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        return headers
    def cookies():
        cookies={'cookie':'browserid=1279509034404673825; steamCountry=CN%7C53f6a00616f7321a48b067c7c4ee3e4b; sessionid=3a16ba3531a20682f9e741ef; timezoneOffset=28800,0; _ga=GA1.2.492800782.1569035619; _gid=GA1.2.727942866.1569035619; app_impressions=755790@1_4_4__100_1|1089350@1_4_4__129_1|755790@1_4_4__100_2|203160:208790:208791:208792:208793:208795:208796:208797:208798:208799:208800:208806:208807:208808:208809:208810:208811:208812:208813:208814:208817:208818@1_4_4__129_3|391220@1_4_4__129_4|850910@1_4_4__129_5|559650@1_4_4__129_6|849260:849261:849262:750920@1_4_4__129_7|1085660:1090200:1090202@1_4_4__129_8|578080@1_4_4__129_9|779340@1_4_4__129_10|382560@1_4_4__129_11|1113910@1_4_4__129_12|629520@1_7_7_151_150_1|479130@1_7_7_151_150_1|518030@1_7_7_151_150_1|413850@1_7_7_151_150_1|730@1_7_7_151_150_1|750920@1_4_4__139_1|617480@1_4_4__43_1; steamLoginSecure=76561198143976330%7C%7CA3376736D41F53D53A4947C2002B8D0774D68A49; steamMachineAuth76561198143976330=74967A266A0EFF7BBFF7B47878760FFFAA820955; recentapps=%7B%22730%22%3A1569036320%7D'}
        return cookies
    def url(headers,cookies):
        url=requests.get(url="https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/",headers=headers,cookies=cookies)
        return url.text
    def page(url):
        page=r'\');">(.+?)</div>'
        page=re.findall(page,url,re.S)
        print(page)
        return page
    def WriterFile(url):
            with open('C:\\Users\\admin\\Desktop\\PythonCode\\SteamTest\\SteamTest\Data.txt','w',newline='',encoding='utf_8_sig') as f:
                f.write(url)
            f.close()
    def init():
        #headers=Tools.headers()
        #cookies=Tools.cookies()
        #url=Tools.url(headers,cookies)
        #Tools.page(url)
        #Tools.WriterFile(url)
        Proxy.Read()
if  __name__=="__main__":
        Tools()
        Tools.init()
