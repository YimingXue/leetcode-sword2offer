#
# @lc app=leetcode.cn id=136 lang=python
#
# [136] 只出现一次的数字
#
# https://leetcode-cn.com/problems/single-number/description/
#
# algorithms
# Easy (60.06%)
# Total Accepted:    55.9K
# Total Submissions: 93.1K
# Testcase Example:  '[2,2,1]'
#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 
# 说明：
# 
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
# 
# 示例 1:
# 
# 输入: [2,2,1]
# 输出: 1
# 
# 
# 示例 2:
# 
# 输入: [4,1,2,1,2]
# 输出: 4
# 
#
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 使用位运算，0异或任何数都是数字本身，任何数字异或它本身都是0
        result = 0
        for item in nums:
            result ^= item
        return result
        
        # 可以用set求和乘2再减去nums
        # summ = sum(set(nums)) * 2
        # return summ - sum(nums)
        

