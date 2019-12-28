#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    #def containsDuplicate(self, nums: List[int]) -> bool:
    def containsDuplicate(self, nums):
        self.nums=nums
        i=0
        for i in range(len(nums)):
            j=nums[i]
            for k in range(len(nums)-1):
                z=nums[k]
                if j>z:
                    num1=j
                    nums[k]=z
                    nums[k+1]=num1
                    flag=-1
        if flag==0:
            return nums      
if __name__=="__main__":
    nums=[1,1,1,3,3,4,3,2,4,2]
    nums_1=Solution().containsDuplicate(nums)
    print(nums)
        # @lc code=end

