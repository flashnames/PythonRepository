import smtplib
import openpyxl
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


def Settings(ServerName):
    SendSettingsDict={}
    if(ServerName=='腾讯'): #如果是腾讯
        SendSettingsDict['LoginAccount']='765719516@qq.com' #验证登陆时的账号,可填写个人或者测试邮箱
        SendSettingsDict['EmailFrom']='765719516@qq.com' #邮件来源
        SendSettingsDict['SendTo']='765719516@qq.com' #发送给谁
        SendSettingsDict['KeyCode']='keuxuwdyughqbfhe' #授权码
        SendSettingsDict['Smtp_Server']='smtp.qq.com' #SMTP服务地址,固定写死
        SendSettingsDict['Smtp_Port']='465' #端口
        return SendSettingsDict
    elif(ServerName=='阿里'): #如果是阿里
        SendSettingsDict['LoginAccount']='junhao.hu@emdoor.com' #验证登陆时的账号,可填写个人或者测试邮箱
        SendSettingsDict['EmailFrom']='junhao.hu@emdoor.com'#邮件来源
        SendSettingsDict['SendTo']='junhao.hu@emdoor.com'#发送给谁
        SendSettingsDict['KeyCode']='MRc720121' #验证密码,填写测试账号或者个人账号密码
        SendSettingsDict['Smtp_Server']='smtp.mxhichina.com' #SMTP服务地址,固定写死
        SendSettingsDict['Smtp_Port']='465' #端口
        return SendSettingsDict #用于SendMail方法调用信息
def SendMail(ServerName):
    try:
        SendSettings={} #初始化字典
        SendSettings=Settings(ServerName) #接收数据
        Msg=Message() #接收邮件内容及附件
        if(ServerName=='腾讯'): #如果是腾讯邮箱
            smtp=smtplib.SMTP_SSL(SendSettings['Smtp_Server'],SendSettings['Smtp_Port']) #服务器smtp地址和端口 阿里已启用25端口
            smtp.login(SendSettings['LoginAccount'],SendSettings['KeyCode']) #登陆验证 腾讯需要开启Smtp服务拿到授权码
            smtp.sendmail(SendSettings['EmailFrom'],SendSettings['SendTo'],Msg.as_string()) #发送邮件以及附件内容
            print("Success Send Email to Tencentmail")
        elif(ServerName=='阿里'): #如果是阿里邮箱
            smtp=smtplib.SMTP_SSL(SendSettings['Smtp_Server'],SendSettings['Smtp_Port']) #服务器smtp地址和端口 阿里已启用25端口
            smtp.login(SendSettings['LoginAccount'],SendSettings['KeyCode']) #登陆验证 阿里不需要授权码但是需要用自己的账号和密码登陆
            smtp.sendmail(SendSettings['EmailFrom'],SendSettings['SendTo'],Msg.as_string()) #发送邮件以及附件内容
            print("Success Send Email to Alimail")
        else:
            print("服务器不存在,请重新输入服务器") #如果都不存在 进入这里弹出提示
    except Exception as E:
        print("Error Info:",E) #出错提示
def Message():
    Msg=MIMEMultipart() #构造邮件对象
    Msg['From']='Test Matchine' #添加一个发件人
    Msg['To']='Test Person' #发送对象
    Msg['Subject']=Header('Test Result','utf-8') #添加邮件主题以及增加对多语言的兼容性
    msg="""
     This is Auto Send Email
     Pls Check Result
    """  #邮件正文,可用中英文
    Text=MIMEText(msg) #将正文添加到类型为MiMEText的text变量中去
    Msg.attach(Text) #将Text变量的值添加到邮件中去
    '''
     上面是发送内容的代码
     -------------------------分割线------------------------
     下面是发送附件的代码
    '''
    File=open('Test.xlsx','rb') #读取文件内容并以字节流传给File变量
    xlsx=MIMEApplication(File.read()) #将读取到的文件内容添加到xlsx变量中去
    xlsx.add_header('content-disposition','attachment',filename='Test.xlsx') 
    '''
     在xlsx中添加头信息的声明,声明该文件的类型以及名字
     如不声明,传输的文件到邮箱中时会变成bin文件或者直接传输字节流信息进邮件中
    '''
    Msg.attach(xlsx) #增加xlsx信息进邮箱对象中去
    return Msg #用于SendMail方法中获取邮件信息
if __name__=="__main__":
    try:
        SendMail('网易') #声明并调用
    except Exception as E:
        print("Error:",E)
