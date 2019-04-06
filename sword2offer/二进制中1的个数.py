# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # 要注意负数的情况
        # 负数在计算机中是以补码的形式存储的
        # 将数字与MASK求与运算就可以得到32位无符号二进制表达方式
        # 例如：同样是-1，直接转换成二进制的结果是'-0b1'
        # 在与MASK与运算后的结果是'0b11111111111111111111111111111111'
        # write code here
        MASK = 0xFFFFFFFF
        binary_n = bin(n & MASK)[2:] 
        return binary_n.count('1')

    def NumberOf1(self, n):
        # 位运算只能针对数字来做，不能对字符串，这种低级错误啊
        MASK = 0xFFFFFFFF
        n = n & MASK
        count = 0
        while n != 0:
            count += 1
            n = (n-1) & n
        return count

if __name__ == '__main__':
    n = 7
    print(Solution().NumberOf1(n))