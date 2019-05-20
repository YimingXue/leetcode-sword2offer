#
# @lc app=leetcode.cn id=371 lang=python
#
# [371] 两整数之和
#
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 需要注意的是在python里如果一个变量初始化是int类型，但是在运算过程中超出了int范围
        # python是会自动将其转成long类型的，因此我们需要用MASK将a，b限制在32位整型范围内
        MAX = 0x7FFFFFFF
        MASK = 0xFFFFFFFF
        
        result = a
        while b:
            result = (a ^ b) & MASK # 与MASK相与则将有符号32位整型转换成了32位无符号整型
            b = ((a & b) << 1) & MASK
            a = result
        return result if result <= MAX else ~(result ^ MASK) # ~(result ^ MASK)操作可以将32位无符号整型转换成32位有符号整型

# # C++写法
# class Solution {
# public:
#     int getSum(int a, int b) {
#         if (b == 0) return a;
#         int sum, carry;
#         sum = a ^ b;
#         carry = a & b;
#         // 需要注意如果carry是负数的话不能直接左移
#         // 因为负数的移位是要保留符号位的，因此要先与INT_MAX与运算将其变成无符号整数
#         if (carry < 0) carry = (carry & INT_MAX) << 1; 
#         else carry <<= 1;
#         return getSum(sum, carry);
#     }
# };
        

