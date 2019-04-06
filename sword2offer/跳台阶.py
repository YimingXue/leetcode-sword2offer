# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 2:
            return number
        else:
            a = 1; b = 2
            for i in range(3, number+1):
                result = a + b
                a = b
                b = result
            return result
    
    def jumpFloor_recursion(self, number):
        # write code here
        if number <= 2:
            return number
        return self.jumpFloor(number-1) + self.jumpFloor(number-2)

if __name__ == "__main__":
    for i in range(1, 10):
        print(Solution().jumpFloor(i))