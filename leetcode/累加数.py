#
# @lc app=leetcode.cn id=306 lang=python
#
# [306] 累加数
#
# https://leetcode-cn.com/problems/additive-number/description/
#
# algorithms
# Medium (29.21%)
# Total Accepted:    1K
# Total Submissions: 3.5K
# Testcase Example:  '"112358"'
#
# 累加数是一个字符串，组成它的数字可以形成累加序列。
# 
# 一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。
# 
# 给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。
# 
# 说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。
# 
# 示例 1:
# 
# 输入: "112358"
# 输出: true 
# 解释: 累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# 
# 
# 示例 2:
# 
# 输入: "199100199"
# 输出: true 
# 解释: 累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
# 
# 进阶:
# 你如何处理一个溢出的过大的整数输入?
# 
#
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i in range(1, len(num)//2+1):
            a = int(num[:i])
            j = 1
            while i+j < (len(num)+i)//2+1:
                b = int(num[i:i+j])
                if self.check(a, b, num):
                    return True
                j += 1
        return False
    
    def check(self, a, b, num):
        c = a + b
        temp = str(a) + str(b) + str(c)
        if temp == num:
            return True
        elif len(temp) > len(num):
            return False
        if temp == num[:len(temp)]:
            return self.check(b, c, num[len(str(a)):])
        else:
            return False
        
if __name__ == '__main__':
    num = "199100199"
    print(Solution().isAdditiveNumber(num))
