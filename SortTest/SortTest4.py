#冒泡排序
import random

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