# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 0:
            return 0
        elif number <= 2:
            return number
        else:
            a = 1
            b = 2
            result = 0
            for i in range(3, number+1):
                result = a + b
                a = b
                b = result
        return result