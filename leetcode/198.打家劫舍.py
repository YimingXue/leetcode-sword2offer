#
# @lc app=leetcode.cn id=198 lang=python
#
# [198] 打家劫舍
#
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# C++写法
# class Solution {
# public:
#     int rob(vector<int>& nums) {
#         if (nums.size() == 0) return 0;
#         if (nums.size() == 1) return nums[0];
#         int maxValue;
#         for (int i=2; i!=nums.size(); i++){
#             maxValue = *max_element(nums.begin(), nums.begin()+i-1);
#             nums[i] += maxValue;
#         }
#         maxValue = *max_element(nums.begin(), nums.end());
#         return maxValue;
#     }
# };  

