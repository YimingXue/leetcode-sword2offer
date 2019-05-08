#
# @lc app=leetcode.cn id=162 lang=python
#
# [162] 寻找峰值
#
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while low < high:
            mid = (low + high) / 2
            if nums[mid] > nums[mid+1]:
                high = mid
            else:
                low = mid + 1
        return low
        

