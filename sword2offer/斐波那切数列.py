# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci_recursion(self, n):
        # 一定记得写退出条件，即n<=0时，直接返回0退出即可
        # 好像上次代码就忘了写这条退出语句了，这么简单的题目啊
        # write code here
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return self.Fibonacci(n-1) + self.Fibonacci(n-2)

    def Fibonacci_list(self, n):
        # write code here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            result = [0, 1, 1]
            for i in range(3, n+1):
                result.append(result[i-1]+result[i-2])
        return result[-1]
    
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a = 0; b = 1
            result = 0
            for i in range(2, n+1):
                result = a + b
                a = b
                b = result
        return result

if __name__ == '__main__':
    n = 10
    for i in range(n):
        print(Solution().Fibonacci_recursion(i), Solution().Fibonacci_list(i), Solution().Fibonacci(i))