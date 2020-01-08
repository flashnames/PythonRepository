#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums,k):
        for i in range(len(nums)):
            num=nums[i]
            for j in range(i+1,len(nums)):
                if num==nums[j]:
                    if abs(j-i)<=k:
                        return True
        return False
    
if __name__=="__main__":
    pr=Solution().containsNearbyDuplicate([1,2,3,1,2,3],2)
    print(pr)
# @lc code=end

