#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.nums=nums
        i=0
        j=1
        k=2
        result=[]
        while(True):
            num1=nums[i]
            num2=nums[j]
            num3=nums[k]
            if num1+num2+num3==0:
                result.append(num1)
                result.append(num2)
                result.append(num3)
            else:
                i+=1
                j+=1
                k+=1
            if k==len(nums):
                break
        return result
# @lc code=end

