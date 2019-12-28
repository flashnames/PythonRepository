class Solution:
    def findNumbers(self, nums) -> int:
        count=0
        for num in nums:
            if num>=10 and num<=100:
                count+=1 
        return count



if __name__=="__main__":
    Solution().findNumbers([12,345,2,6,7896])
