#选择排序
import random

def SortTest(List):
    min_index=0 
    for i in range(len(List) - 1):
           # 将起始元素设为最小元素
        min_index = i
          # 第二层for表示最小元素和后面的元素逐个比较
        for j in range(i + 1, len(List)):
            if List[min_index]>List[j]:
                # 如果当前元素比最小元素小，则把当前元素角标记为最小元素角标
                min_index = j
         # 查找一遍后将最小元素与起始元素互换
        num1=List[i]
        List[i]=List[min_index]
        List[min_index]=num1
    return List

if __name__=="__main__":
    TestList=[]
    for i in range(10):
        rannum=random.randint(0,100)
        TestList.append(rannum)
    List=SortTest(TestList)
    print(List)