import time
from appium import webdriver
import random
import requests

WifiName=["EM-public","ASUS"]
WifiList=["three bars","signal full"]
size={}

def dc_option():
    desire_caps={}
    desire_caps['platformName']='Android'
    desire_caps['playformVersion']='8.1'
    desire_caps['deviceName']='0123456789ABCDEF'
    #desire_caps['noReset']=True
    desire_caps['automationName']='Appium'
    desire_caps['appPackage']='com.android.launcher3'
    desire_caps['appActivity']='com.android.launcher3.Launcher'
    desire_caps['appWaitActivity']='com.android.launcher3.Launcher'
    desire_caps['newCommandTimeout']=5000
    desire_caps['resetKeyboard']=False
    return desire_caps
#-----------BeforeTest------------------------------------------

def get_size():
    x=driver.get_window_size()['width']
    y=driver.get_window_size()['height']
    return(x,y)

def swipe_top(size,time):
    x_1=int(size[0]*0.2)
    x_2=int(size[0]*0.3)
    y_1=int(size[1]*0.75)
    y_2=int(size[1]*0.15)
    driver.swipe(x_1,y_1,x_2,y_2,time)

def swipe_down():
    driver.swipe(809,9,885,212,500)

def swipe_down_1():
    driver.swipe(712,6,714,462,500)
def swipe_top_1():
    driver.swipe(503,1079,494,793,500)


def OpenGetPowerApp():
    driver.find_element_by_accessibility_id("GetPower").click()
    driver.find_element_by_id('com.example.GetPower:id/getPower').click()
    driver.press_keycode(3)


def CloseWifi():
    driver.find_element_by_xpath('//android.widget.Switch'
    +'[@content-desc="Wi-Fi,Wi-Fi '
    +WifiList[1]
    +'.,'
    +WifiName[1]
    +'"]'
    +'/android.widget.FrameLayout/android.view.ViewGroup/'
    +'android.widget.FrameLayout/android.widget.ImageView').click()
def CloseWifi_1():
    driver.find_element_by_xpath('//android.widget.Switch'
    +'[@content-desc="Wi-Fi,Wi-Fi '
    +WifiList[1]
    +'.,'
    +WifiName[1]
    +'"]'
    +'/android.widget.FrameLayout/android.view.ViewGroup/'
    +'android.widget.FrameLayout/android.widget.ImageView').click()

def OpenWifi():
    driver.find_element_by_xpath('//android.widget.Switch[@content-desc="Wi-Fi,"]'
    +'/android.widget.FrameLayout/android.view.ViewGroup').click()
    size=get_size()
    swipe_top(size,500)

#--------------------------Tencent Video------------------
def TententVideo():
    driver.find_element_by_accessibility_id('Tencent Video').click()
    time.sleep(10)
    driver.find_element_by_id('com.tencent.qqlive:id/a76').click()
    time.sleep(4)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/'
    +'android.widget.LinearLayout/'
    +'android.widget.FrameLayout/'
    +'android.widget.LinearLayout/'
    +'android.widget.LinearLayout/'
    +'android.widget.FrameLayout/'
    +'android.widget.LinearLayout/'
    +'android.widget.RelativeLayout[1]/'
    +'android.widget.LinearLayout/'
    +'android.support.v7.widget.RecyclerView/'
    +'android.widget.RelativeLayout[3]/android.widget.TextView').click()

    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/'
    +'android.widget.LinearLayout/'
    +'android.widget.FrameLayout/'
    +'android.widget.LinearLayout/'
    +'android.widget.LinearLayout/'
    +'android.widget.FrameLayout/'
    +'android.widget.LinearLayout/'
    +'android.widget.RelativeLayout[2]/'
    +'android.widget.LinearLayout/'
    +'android.support.v4.view.ViewPager/'
    +'android.widget.RelativeLayout/'
    +'android.widget.LinearLayout/'
    +'android.widget.FrameLayout/'
    +'android.support.v7.widget.RecyclerView/'
    +'android.widget.RelativeLayout[1]/'
    +'android.widget.RelativeLayout/'
    +'android.widget.LinearLayout').click()

    time.sleep(3)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/'
    +'android.widget.LinearLayout/'
    +'android.widget.FrameLayout/'
    +'android.widget.LinearLayout/'
    +'android.widget.LinearLayout/'
    +'android.widget.LinearLayout/'
    +'android.widget.FrameLayout/'
    +'android.widget.LinearLayout/'
    +'android.widget.FrameLayout/'
    +'android.support.v7.widget.RecyclerView/'
    +'android.widget.LinearLayout[2]/'
    +'android.widget.RelativeLayout').click()
    time.sleep(120)
    driver.find_element_by_id('com.tencent.qqlive:id/bju').click()
    driver.find_element_by_id('com.tencent.qqlive:id/bts').click()

def OpenTencentVideo(size):
    time.sleep(2)
    swipe_down()
    OpenWifi() #打开wifi
    time.sleep(4)
    swipe_top(size,500)
    TententVideo()
    driver.press_keycode(4) #调用返回键
    swipe_down_1() #下拉状态框
    CloseWifi()  #关闭wifi 
    swipe_top(size,500) #上拉状态框
    driver.press_keycode(3) #调用home
    time.sleep(2) 
    swipe_top(size,500) #上拉屏幕
    time.sleep(2)
    OpenGetPowerApp() #获取电量
    print("Tencent Video Test Finish")
#---------------------Tencent Video End-------------------------------------------------------------
def OpenGame():
    driver.find_element_by_accessibility_id('NFS Most Wanted').click()
    time.sleep(60)
    driver.press_keycode(3)
    print("Game Test Finish")

def record():
    driver.tap([(497,1106),(500,1109)],200)
    time.sleep(2)
    driver.tap([(397,1076),(397,1076)],200)
    time.sleep(300)
    driver.tap([(397,1076),(397,1076)],200)
    driver.press_keycode(3)
    return

def OpenCamera():
       driver.find_element_by_accessibility_id('Camera').click()
       for i in range(30):
            time.sleep(30)
            driver.press_keycode(27)
            i=i+1
            print(i)
       record()
       print("Camera Test Finish")

def OpenMusic(size):
    swipe_top(size,500)
    driver.find_element_by_accessibility_id('Play Music').click()
    time.sleep(3)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/'
    +'android.widget.LinearLayout/'
    +'android.widget.FrameLayout/'
    +'android.widget.LinearLayout/'
    +'android.widget.FrameLayout/'
    +'android.support.v4.widget.DrawerLayout/'
    +'android.widget.FrameLayout/'
    +'android.widget.LinearLayout/'
    +'android.view.ViewGroup/'
    +'android.widget.FrameLayout/'
    +'android.widget.FrameLayout[3]/'
    +'android.support.v7.widget.RecyclerView/'
    +'android.widget.LinearLayout/'
    +'android.widget.LinearLayout[2]/'
    +'android.widget.RelativeLayout[2]/'
    +'android.widget.ImageView[1]').click()
    driver.find_element_by_accessibility_id('Play').click()
    driver.press_keycode(26)
    time.sleep(3)
    driver.press_keycode(26)
    swipe_top(size,500)
    time.sleep(3)
    driver.press_keycode(3)
    time.sleep(3)
    swipe_top(size,500)
    driver.find_element_by_accessibility_id('Play Music').click()
    driver.find_element_by_accessibility_id('Play').click()
    driver.press_keycode(3)
    time.sleep(3)
    swipe_top(size,500)
    OpenGetPowerApp()
    print("Music Test Finish")
    
def OpenBrowser():
      driver.find_element_by_accessibility_id('Chrome').click()
      driver.find_element_by_id('com.android.chrome:id/url_bar').clear()
      driver.find_element_by_id('com.android.chrome:id/url_bar').send_keys('http://www.tclcom.com/test/')
      driver.press_keycode(66)
      time.sleep(1800)
      driver.press_keycode(4)
      swipe_top_1()
      OpenGetPowerApp()
      Print("Browser Test Finish")

def OpenWeiBo(size):
    swipe_top(size,500)
    driver.find_element_by_accessibility_id('Weibo').click()
    time.sleep(3)
    for second in range(10):
        time.sleep(20)
        driver.swipe(473,1103,465,247,500)
        second=second+1
        if second==3:
            print(second)
            break
        driver.press_keycode(3)
        print("WeiBo Test Finish")

def OpenWeChat(size):
    driver.find_element_by_accessibility_id('WeChat').click()
    time.sleep(10)
    driver.find_element_by_id('com.tencent.mm:id/qi').click()
    driver.find_element_by_id('com.tencent.mm:id/li').send_keys('WeChat Team')
    driver.find_element_by_id('com.tencent.mm:id/rd').click()
    driver.find_element_by_accessibility_id('Comments').click()
    for i in range(3):
        Rnum=random.randint(0,29)
        driver.find_element_by_id('com.tencent.mm:id/aom').clear()
        driver.find_element_by_id('com.tencent.mm:id/aom').send_keys('Message%d'%Rnum)
        driver.find_element_by_id('com.tencent.mm:id/aot').click()
        time.sleep(60)
        i=i+1
    driver.press_keycode(3)
    swipe_top(size,500)
    OpenGetPowerApp()
    print("WeChat Test Finish")

def CheckGetPower(size):
    swipe_top(size,500)
    AppStatus=driver.is_app_installed("com.example.GetPower")
    if AppStatus:
        return
    else:
        driver.install_app("https://raw.githubusercontent.com/flashnames/ApkRepository/master/GetPower.apk?token=ALIUASK3HON674SDBP42F5K5LO6PO")
def init():
    size=get_size()
    CheckGetPower(size)
    #OpenGame()
    OpenMusic(size)
    OpenTencentVideo(size)
    OpenCamera()
    OpenBrowser()
    OpenWeiBo(size)
    OpenWeChat(size)

if __name__=="__main__":
    driver=webdriver.Remote("http://localhost:4723/wd/hub",dc_option())
    time.sleep(3)
    init()
    