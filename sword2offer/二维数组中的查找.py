# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if array == None or len(array) <= 0:
            return False
        col = len(array)
        row = len(array[0])
        m = col - 1
        n = 0
        while m >= 0 and n < row:
            if array[m][n] == target:
                return True
            elif array[m][n] < target:
                n += 1
            elif array[m][n] > target:
                m -= 1
        return False