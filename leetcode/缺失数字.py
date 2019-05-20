#
# @lc app=leetcode.cn id=268 lang=python
#
# [268] 缺失数字
#
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # maxInt = len(nums)+1
        # for i in range(maxInt+1):
        #     if i not in nums:
        #         return i
        n = len(nums)
        return (n * (n+1) / 2) - sum(nums)
 
#  # C++写法
# class Solution {
# public:
#     int missingNumber(vector<int>& nums) {
#         double sum = (float)(1 + nums.size()) / 2 * nums.size();
#         int current_sum = 0;
#         for (int item : nums){
#             current_sum += item;
#         }
#         return sum - current_sum;
#     }
# };
        

