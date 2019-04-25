#
# @lc app=leetcode.cn id=264 lang=python
#
# [264] 丑数 II
#
# https://leetcode-cn.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (41.92%)
# Total Accepted:    4.4K
# Total Submissions: 10.3K
# Testcase Example:  '10'
#
# 编写一个程序，找出第 n 个丑数。
# 
# 丑数就是只包含质因数 2, 3, 5 的正整数。
# 
# 示例:
# 
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
# 
# 说明:  
# 
# 
# 1 是丑数。
# n 不超过1690。
# 
# 
#
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [1]
        index2 = 0; index3 = 0; index5 = 0
        while len(result) < n:
            temp = min(result[index2]*2, result[index3]*3, result[index5]*5)
            result.append(temp)
            if temp == result[index2]*2:
                index2 += 1
            if temp == result[index3]*3:
                index3 += 1
            if temp == result[index5]*5:
                index5 += 1
        return result[-1]

# # C++写法
# class Solution {
# public:
#     int nthUglyNumber(int n) {
#         if (n==1) return 1;
#         vector<int> result{1};
#         int index2=0, index3=0, index5=0;
#         while (result.size()<n)
#         {
#             int min = minNumber(result[index2]*2, result[index3]*3, result[index5]*5);
#             result.push_back(min);
#             if (min==result[index2]*2) index2+=1;
#             if (min==result[index3]*3) index3+=1;
#             if (min==result[index5]*5) index5+=1;
#         }
#         return result[result.size()-1];
#     }
    
#     int minNumber(int a, int b, int c){
#         int min = a<b?a:b;
#         min = min<c?min:c;
#         return min;
#     }
# };
        

