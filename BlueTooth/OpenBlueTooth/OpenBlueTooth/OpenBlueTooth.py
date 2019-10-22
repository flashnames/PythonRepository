from appium import webdriver
import random
import time

Text="null"
i=0

def dc_option():
        desire_caps={}
        desire_caps['platformName']='Android'
        desire_caps['playformVersion']='9'
        desire_caps['deviceName']='0123456789ABCDEF'
        desire_caps['automationName']='Appium'
        desire_caps['appPackage']='com.android.launcher3'
        desire_caps['appActivity']='com.android.searchlauncher.SearchLauncher'
        desire_caps['appWaitActivity']='com.android.searchlauncher.SearchLauncher'
        desire_caps['newCommandTimeout']=10000
        desire_caps['resetKeyboard']=False
        return desire_caps

driver=webdriver.Remote("http://localhost:4723/wd/hub",dc_option())


class Tools:
   def get_size():
        x=driver.get_window_size()['width']
        y=driver.get_window_size()['height']
        print((x,y))
        return(x,y)

   def Swipe_Menu(size,time): #上拉菜单
        x_1=int(size[0]*0.2)
        x_2=int(size[0]*0.3)
        y_1=int(size[1]*0.75)
        y_2=int(size[1]*0.15)
        driver.swipe(x_1,y_1,x_2,y_2,time)

class BlueTest:
    def OpenSettings():
        driver.find_element_by_accessibility_id('Settings').click()

    def CdBlueTooth():
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.TextView[1]').click()
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[4]').click()
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout').click()

    def OpenBlueTooth():
        driver.find_element_by_id('com.android.settings:id/switch_widget').click()
   
    def GetText():
        Text=driver.find_element_by_id('com.android.settings:id/switch_text').text
        return Text

    def press_keycode(size):
        driver.press_keycode(3)
        time.sleep(3)
        Tools.Swipe_Menu(size,1000)
        time.sleep(3)
        BlueTest.OpenSettings()
        time.sleep(3)
        BlueTest.CdBlueTooth()
        time.sleep(3)
        driver.press_keycode(4)
        time.sleep(3)
        driver.press_keycode(26)
        time.sleep(3)
        driver.press_keycode(26)
        time.sleep(3)
        for i in range(4):
            driver.press_keycode(25)
        for i in range(4):
            driver.press_keycode(24)
        time.sleep(3)
        driver.press_keycode(3)

    def rename():
        num=random.randint(1,100)
        BlueTest.OpenSettings()
        BlueTest.CdBlueTooth()
        Text=BlueTest.GetText()
        time.sleep(3)
        if(Text=="On"):
            time.sleep(3)
            driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout').click()
            driver.find_element_by_id('com.android.settings:id/edittext').clear()
            driver.find_element_by_id('com.android.settings:id/edittext').send_keys('smart tab %d'%num)
            driver.find_element_by_id('android:id/button1').click()
            TestName=driver.find_element_by_id('android:id/summary').text
            print(TestName)
            if(TestName!='smart tab %d'%num):
                print('Error with ReName')
        else:
            BlueTest.OpenBlueTooth()
    def init():
        time.sleep(3)
        size=Tools.get_size()
        Tools.Swipe_Menu(size,1000)
        BlueTest.OpenSettings()
        time.sleep(3)
        BlueTest.CdBlueTooth()
        #for j in range(60):
            #Text=BlueTest.GetText()
            #if(Text=="On"):
                #i=i+1
                #print(i)
            #BlueTest.OpenBlueTooth()
        time.sleep(3)
        BlueTest.press_keycode(size)
        BlueTest.rename()
        
if __name__=="__main__":
    BlueTest()
    BlueTest.init()