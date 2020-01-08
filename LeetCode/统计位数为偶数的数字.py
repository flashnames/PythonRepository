class Solution:
    def findNumbers(self, nums):
        List=[]
        Count=0
        for num in nums:
            num=str(num)
            List=list(num)
            if len(List)%2==0:
                Count+=1
        return Count
if __name__=="__main__":
    print(Solution().findNumbers([12,345,2,6,7896]))
