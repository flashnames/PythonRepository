#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1,nums2) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range((len(nums1)-len(nums2)),len(nums1)):
            if nums1[i]==0:
                num=nums2.pop(0)
                nums1[i]=num
        for i in range(len(nums1)):
            key=i
            for j in range(i+1,len(nums1)):
                if nums1[key]>nums1[j]:
                    key=j
            num=nums1[i]
            nums1[i]=nums1[key]
            nums1[key]=num
        print(nums1)



if __name__=="__main__":
    Solution().merge([1,2,3,0,0,0],[2,5,6])
# @lc code=end

