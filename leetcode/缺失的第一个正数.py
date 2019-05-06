#
# @lc app=leetcode.cn id=41 lang=python
#
# [41] 缺失的第一个正数
#
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]:
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1

# # C++写法
# class Solution {
# public:
#     int firstMissingPositive(vector<int>& nums) {
#         int i = 0;
#         while (i < nums.size())
#         {
#             if (nums[i]>0 && nums[i]<=nums.size() && nums[nums[i]-1]!=nums[i] && nums[i]!=i+1)
#             {
#                 int temp = nums[nums[i]-1];
#                 nums[nums[i]-1] = nums[i];
#                 nums[i] = temp;
#             }
#             else
#             {
#                 i += 1;
#             }
#         }
#         for (int i=0; i<nums.size(); i++)
#         {
#             if (nums[i]!=i+1)
#             {
#                 return i+1;
#             }
#         }
#         return nums.size()+1;
#     }
# };
        

