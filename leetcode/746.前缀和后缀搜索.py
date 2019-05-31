#
# @lc app=leetcode.cn id=746 lang=python
#
# [746] 前缀和后缀搜索
#
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
# C++写法
# class Solution {
# public:
#     int minCostClimbingStairs(vector<int>& cost) {
#         // if (cost.size() == 0) return 0;
#         // if (cost.size() <= 2) return *min_element(cost.begin(), cost.end());
#         // for (int i = 2; i != cost.size(); i++){
#         //     if (cost[i] + cost[i-1] < cost[i] + cost[i-2]) cost[i] = cost[i] + cost[i-1];
#         //     else cost[i] = cost[i] + cost[i-2];
#         // }
#         // if (cost.back() < cost[cost.size()-2]) return cost.back();
#         // else return cost[cost.size()-2];
        
#         if (cost.empty()) return 0;
#         vector<int> dp(cost.size());
#         dp[0] = 0;
#         dp[1] = min(cost[0], cost[1]);
#         for (int i = 2; i != cost.size(); i++){
#             dp[i] = min(dp[i-2] + cost[i-1], dp[i-1] + cost[i]);
#         }
#         return dp.back();
#     }
# };

