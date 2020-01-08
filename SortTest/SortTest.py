import random


#冒泡排序
'''
已知一组无序数据a[1]、a[2]、……a[n]，
需将其按升序排列。首先比较a[1]与a[2]的值，
若a[1]大于a[2]则交换两者的值，否则不变。再比较a[2]与a[3]的值，
若a[2]大于a[3]则交换两者的值，否则不变。再比较a[3]与a[4]，
以此类推，
最后比较a[n-1]与a[n]的值。
这样处理一轮后，
a[n]的值一定是这组数据中最大的。
再对a[1]~a[n-1]以相同方法处理一轮，
则a[n-1]的值一定是a[1]~a[n-1]中最大的。
再对a[1]~a[n-2]以相同方法处理一轮，以此类推。
共处理n-1轮后a[1]、a[2]、……a[n]就以升序排列了。
降序排列与升序排列相类似，若a[1]小于a[2]则交换两者的值，
否则不变，后面以此类推。 
总的来讲，每一轮排序后最大（或最小）的数将移动到数据序列的最后，
理论上总共要进行n(n-1）/2次交换
'''


def SortTest(List):
    for i in range(len(List)):
        for j in range(len(List)-i-1):
            if List[j]>List[j+1]:
                num=List[j]
                List[j]=List[j+1]
                List[j+1]=num 
    return List
if __name__=="__main__":
    TestList=[]
    for i in range(10):
        rannum=random.randint(0,100)
        TestList.append(rannum)
    print(TestList)
    List=SortTest(TestList)
    print(List)