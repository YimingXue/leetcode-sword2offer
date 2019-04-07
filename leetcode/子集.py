#
# @lc app=leetcode.cn id=78 lang=python
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (72.13%)
# Total Accepted:    15.8K
# Total Submissions: 21.9K
# Testcase Example:  '[1,2,3]'
#
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: nums = [1,2,3]
# 输出:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 从位运算的角度思考，如果nums中有三个数字，则可以想象成是三位的二进制，
        # 则可表示为'000','001','010'...
        # 如果把1表示为取当前数字，o表示为不取当前数字，则可以实现对所有可能情况的列举
        # 需要注意的是数字转换成二进制时需要左边补零到nums长度，这里搞了好久
        # length = len(nums)
        # max_size = 2**length
        # result = list()
        # for i in range(max_size):
        #     temp = list()
        #     binary_i = bin(i)[2:].zfill(len(nums))
        #     for j in range(len(binary_i)):
        #         if binary_i[j] == '1':
        #             temp += [nums[j]]
        #     result.append(temp)
        # return result
        
        # 增量构造大法，遍历数组，每遇到一个新的数字，就添加到新建的之前所有数组元素中
        # 需要注意的是python在循环过程中是会一直更新列表的，所以内层循环需要使用深拷贝列表
        result = [[]]
        for num in nums:
            temp = result[:]
            for item in temp:
                result.append(item+[num])
        return result
        

