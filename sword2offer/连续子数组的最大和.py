# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        max_number = array[0]
        for i in range(1, len(array)):
            if array[i-1] >= 0:
                array[i] += array[i-1]
            if array[i] > max_number:
                max_number = array[i]
        return max_number

# # C++写法
# class Solution {
# public:
#     int FindGreatestSumOfSubArray(vector<int> array) {
#         if (array.size()<0) return -1;
#         int maxSum = array[0];
#         for (int i=1; i<array.size(); i++){
#             if (array[i-1]>0){
#                 array[i] += array[i-1];
#             }
#             if (array[i]>maxSum){
#                 maxSum = array[i];
#             }
#         }
#         return maxSum;
#     }
# };