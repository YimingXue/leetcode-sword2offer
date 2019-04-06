#
# @lc app=leetcode.cn id=190 lang=python
#
# [190] 颠倒二进制位
#
# https://leetcode-cn.com/problems/reverse-bits/description/
#
# algorithms
# Easy (37.67%)
# Total Accepted:    10.8K
# Total Submissions: 28.5K
# Testcase Example:  '00000010100101000001111010011100'
#
# 颠倒给定的 32 位无符号整数的二进制位。
# 
# 
# 
# 示例 1：
# 
# 输入: 00000010100101000001111010011100
# 输出: 00111001011110000010100101000000
# 解释: 输入的二进制串 00000010100101000001111010011100 表示无符号整数 43261596，
# ⁠     因此返回 964176192，其二进制表示形式为 00111001011110000010100101000000。
# 
# 示例 2：
# 
# 输入：11111111111111111111111111111101
# 输出：10111111111111111111111111111111
# 解释：输入的二进制串 11111111111111111111111111111101 表示无符号整数 4294967293，
# 因此返回 3221225471 其二进制表示形式为 10101111110010110010011101101001。
# 
# 
# 
# 提示：
# 
# 
# 请注意，在某些语言（如
# Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
# 在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 2 中，输入表示有符号整数 -3，输出表示有符号整数
# -1073741825。
# 
# 
# 
# 
# 进阶:
# 如果多次调用这个函数，你将如何优化你的算法？
# 
#
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # 转换成二进制，左边补零至32位，翻转字符串然后转换成数字即可 
        
        # binary_n = bin(n)[2:]
        # len_binary_n = len(binary_n)
        # if len_binary_n < 32:
        #     for i in range(32-len_binary_n, 0, -1):
        #         binary_n = '0' + binary_n
        # binary_n = binary_n[::-1]
        # return int(binary_n, 2)

        # binary_n = '{0:032b}'.format(n)[::-1]
        # return int(binary_n, 2)

        # return int(bin(n)[2:].zfill(32)[::-1], 2)
        
        # 这里注意rjust是右边对齐，并不是右边补零
        return int(bin(n)[2:].rjust(32, '0')[::-1], 2)


if __name__ == '__main__':
    n = 2
    # print(Solution().reverseBits(n))
    result = '{0:032b}'.format(n)
    print(result, len(result))

