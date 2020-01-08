#插入排序
import random

def SortTest(arr): 
  
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
    return arr

if __name__=="__main__":
    TestList=[]
    for i in range(10):
        rannum=random.randint(0,100)
        TestList.append(rannum)
    List=SortTest(TestList)
    print(List)

