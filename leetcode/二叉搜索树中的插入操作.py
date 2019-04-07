#
# @lc app=leetcode.cn id=784 lang=python
#
# [784] 二叉搜索树中的插入操作
#
# https://leetcode-cn.com/problems/letter-case-permutation/description/
#
# algorithms
# Easy (52.15%)
# Total Accepted:    3.8K
# Total Submissions: 7.3K
# Testcase Example:  '"a1b2"'
#
# 给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。
# 
# 
# 示例:
# 输入: S = "a1b2"
# 输出: ["a1b2", "a1B2", "A1b2", "A1B2"]
# 
# 输入: S = "3z4"
# 输出: ["3z4", "3Z4"]
# 
# 输入: S = "12345"
# 输出: ["12345"]
# 
# 
# 注意：
# 
# 
# S 的长度不超过12。
# S 仅由数字和字母组成。
# 
# 
#
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
#         # 使用递归完成，每次修改其中一个字母的大小写
#         # 我完成的这个代码缺点在于会有重复计算
#         self.result = list()
#         fixIndex = 0
#         self.recursion(fixIndex, S)
#         return self.result
    
#     def recursion(self, fixIndex, S):
#         S_temp = S[:]
#         while fixIndex < len(S_temp) and S_temp[fixIndex].isdigit():
#             fixIndex += 1
#         if fixIndex >= len(S_temp):
#             self.result.append(S_temp)
#             return
#         self.recursion(fixIndex+1, S_temp[:fixIndex]+S_temp[fixIndex].lower()+S_temp[fixIndex+1:])
#         self.recursion(fixIndex+1, S_temp[:fixIndex]+S_temp[fixIndex].upper()+S_temp[fixIndex+1:])
        
        # 遍历整个字符串，如果当前元素为数字，则为结果数组中每个字符串都添加这个数字
        # 如果当前元素为字母，则为当前结果数组中所有元素添加当前小写字母，并生成新的添加当前大写字母的字符串
        result = ['']
        for s in S:
            if s.isdigit():
                for i in range(len(result)):
                    result[i] += s
            else:
                for i in range(len(result)):
                    temp = result[i]
                    result[i] += s.lower()
                    result.append(temp+s.upper())
        return result
        

