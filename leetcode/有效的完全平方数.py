#
# @lc app=leetcode.cn id=367 lang=python
#
# [367] 有效的完全平方数
#
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # n = 0
        # if num == 0:
        #     return False
        # while n*n <= num:
        #     if n*n == num:
        #         return True
        #     n += 1
        # return False
        
        if num == 0:
            return False
        left = 0
        right = num
        while left <= right:
            mid = (left + right) / 2
            n = mid * mid
            if n == num:
                return True
            elif n > num:
                right = mid - 1
            elif n < num:
                left = mid + 1
        return False
        

