# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number <= 2:
            return number
        return 2 ** (number-1)
    def jumpFloorII(self, number):
    # write code here
    if number == 1:
        return number
    return 2*self.jumpFloorII(number-1)