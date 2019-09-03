import requests
import re
Tables=r'<li>(.+?)</li>'
Listeners=r'<span class="nb">(.+?)</span>'
Titles=r'class="tit f-thide s-fc0">(.+?)</a>'
UserNames=r'class="nm nm-icn f-thide s-fc3">(.+?)</a>'
Links=r'data-res-id="(.+?)"'
Listener=[]
Title=[]
UserName=[]
Link=[]
j=0
num=0
class NetMusic(object):
    def cookies():
        cookies={'cookie':'td_cookie=1058838974; _iuqxldmzr_=32; _ntes_nnid=43cb5bea832ab0ac4ada22158caf8c75,1566800720426; _ntes_nuid=43cb5bea832ab0ac4ada22158caf8c75; WM_TID=2zlOI%2FLUw6JAAEQQRFc4pLW1wsPnXjxX; ntes_kaola_ad=1; __remember_me=true; vjuids=-530ad98bc.16cd77b4fbf.0.edc7163dbdf51; vjlast=1566983279.1566983279.30; vinfo_n_f_l_n3=0541a43af221cfa6.1.0.1566983278681.0.1566983323670; WM_NI=KIcFspwuBNq3doYxfg%2BGy%2BXxFPAgooO62H3k0TVltU8Xl3%2BBCjeBR7IgCx1a3s2UgrunLY%2BJklDtMw4T0UCF1d8HDNFq9Dk1qz4mt5t7aFxXXFH3xPjj%2Fa7CilXAGc3raE8%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeaaf960f7f0bfa8e1449ab08fb2c44e879e8b84f73f89eb9fd8eb3a93b8b68cc92af0fea7c3b92a8997ada7f27cb5ab8eaff439a8b19799e56de999b7ccdb7486908f88ee658deafea9b261f48c9a8df75ffc88a4d4aa4a81b6aba3d13d8bb98d99b46bf1adfeb6e67ab7b284baaa42a9b48c95d07df88c00b6c24ef3bcf8a9c74686aff7a5ea3bb3a6fc8ef73fb8e9afa7fb549c9a88d4fb5caab6e182b649abb498a2c669f1aeafa6bb37e2a3; JSESSIONID-WYYY=QveTq13w%2BpngAtyPm7O0cPOlxvUjn1JpfGF0NmAeZnGSDkF40GQ%2B8pYqeBv0KX%5C%2BbaVvpEx6BnGAqkUzcRtuf4V6IUYft8fESyKJ%5CejyIv%2FRoVp%2BCq%2B5gm01aP23IT6fsA7eNMpVNrMiY6kJCq4T2plVac8zxNSw347grk8XUFTsR3Fm%3A1567417543391; MUSIC_U=ca5868dc0a0e3afacdb2848fba260da06743b912f50e53d14377f72636b7e778189dcb504712a30c877e2d8aaa899d9cdd82a30a659dcf5f10a819cd9ae51d4e5d3ee6d23140fc66bf122d59fa1ed6a2; __csrf=9b0ca693101761d41d3d29f0970af6f0'}
        return cookies
    def headers():
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
        return headers
    def url(headers,cookies):
        url=requests.get(url='https://music.163.com/discover/playlist',headers=headers,cookies=cookies)
        return url.text
    def Page(url):
        Total=r'<ul class="m-cvrlst f-cb" id="m-pl-container">(.+?)</ul>'
        page=re.findall(Total,url,re.S)
        return page
    def MaxNumber():
        Numbers=r'class="zpgi">38</a>'
    def Read(page):
        global j
        Tables=r'<li>(.+?)</li>'
        for info in page:
            GetTable=re.findall(Tables,info,re.S)
            for Line in GetTable:
                GetListeners=re.findall(Listeners,Line,re.S)
                Listener.insert(j,GetListeners[0])
                GetName=re.findall(UserNames,Line,re.S)
                UserName.insert(j,GetName[0])
                GetTitle=re.findall(Titles,Line,re.S)
                Title.insert(j,GetTitle[0])
                GetLink=re.findall(Links,Line,re.S)
                Link.insert(j,GetLink[0])
                j+=1
    def ReadData(headers,page):
        global num
        num+=35
        cookies=NetMusic.cookies()
        url=requests.get(url='https://music.163.com/discover/playlist/?order=hot&cat=全部&limit=35&offset=%d'%num,headers=headers,cookies=cookies,)
        page=NetMusic.Page(url.text)
        NetMusic.Read(page)
    def init():
        cookies=NetMusic.cookies()
        headers=NetMusic.headers()
        url=NetMusic.url(headers,cookies)
        page=NetMusic.Page(url)
        NetMusic.Read(page)
        NetMusic.ReadData(headers,page)

if __name__=="__main__":
    NetMusic()
    NetMusic.init()



#无法翻页