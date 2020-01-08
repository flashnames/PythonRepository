import random



def Test(nums):
    flag=True
    for i in range(len(nums)):
        num=nums[i]
        for j in range(len(nums)-1):
            data=nums[j]
            nums[j]=nums[j+1]
            nums[j+1]=data
            print(nums)
    return nums
    


if __name__=="__main__":
    nums=[]
    nums=random.sample(range(1,5),3)
    print(nums)
    pr=Test(nums)