# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        pushV = pushV[::-1]
        popV = popV[::-1]
        stack = list()
        while pushV:
            temp = pushV.pop()
            if temp == popV[-1]:
                popV.pop()
                continue
            else:
                stack.append(temp)
        if stack == popV:
            return True
        else:
            return False