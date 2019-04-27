#
# @lc app=leetcode.cn id=279 lang=python
#
# [279] 完全平方数
#
# https://leetcode-cn.com/problems/perfect-squares/description/
#
# algorithms
# Medium (48.63%)
# Total Accepted:    8.9K
# Total Submissions: 18.1K
# Testcase Example:  '12'
#
# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
# 
# 示例 1:
# 
# 输入: n = 12
# 输出: 3 
# 解释: 12 = 4 + 4 + 4.
# 
# 示例 2:
# 
# 输入: n = 13
# 输出: 2
# 解释: 13 = 4 + 9.
# 
#
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 使用动态规划，result[i]存储的是组成i这个数值的最小完全平方数个数
        # 对于i这个数字来说，如果能表示成a+b*b这种形式，则result[i]为result[i]当前数值或result[a]+1中，因为b*b构成了一个完全平方数
        result = [float('inf') for _ in range(n+1)]
        result[0] = 0
        for i in range(n+1):
            j = 1
            while i+j*j <= n:
                result[i+j*j] = min(result[i+j*j], result[i]+1)
                j += 1
        return result[n]

# # C++写法
# class Solution {
# public:
#     int numSquares(int n) {
#         vector<int> dp(n+1, INT_MAX);
#         dp[0] = 0;
#         for (int i=0; i<=n; i++)
#         {
#             for (int j=1; i+j*j<=n; j++)
#             {
#                 dp[i+j*j] = min(dp[i+j*j], dp[i]+1);
#             }
#         }
#         return dp[n];
#     }
# };
        

