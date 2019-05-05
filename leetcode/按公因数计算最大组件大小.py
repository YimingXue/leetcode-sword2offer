#
# @lc app=leetcode.cn id=989 lang=python
#
# [989] 按公因数计算最大组件大小
#
class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        if K == 0:
            return A
        # num = 0
        # for i in range(len(A)):
        #     num = num*10 + A[i]
        A = int(''.join(list(map(str, A))))
        num = A + K
        # result = []
        # while num != 0:
        #     result.append(num%10)
        #     num /= 10
        # return result[::-1]
        return list(map(int, str(num)))

