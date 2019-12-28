#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums=nums
        self.target=target
        size=len(nums)
        for i in range(0,size):
            for j in range(i+1,size):
                result=nums[i]+nums[j]
                if(result==target):
                    return [i,j]
# @lc code=end

