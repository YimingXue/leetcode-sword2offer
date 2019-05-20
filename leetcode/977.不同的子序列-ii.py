#
# @lc app=leetcode.cn id=977 lang=python
#
# [977] 不同的子序列 II
#
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        # result = list()
        # for item in A:
        #     result.append(item**2)
        #     i = len(result) - 1
        #     while i > 0 and result[i-1] >= item**2:
        #         result[i] = result[i-1]
        #         i -= 1
        #     result[i] = item**2
        # return result
        
        length = len(A)
        left = 0
        right = length - 1
        current = length - 1
        result = [0] * length
        while left <= right:
            L = A[left] ** 2
            R = A[right] ** 2
            if L <= R:
                result[current] = R
                right -= 1
                current -= 1
            else:
                result[current] = L
                left += 1
                current -= 1
        return result

# # C++写法
# class Solution {
# public:
#     vector<int> sortedSquares(vector<int>& A) {
#         int length = A.size();
#         int left = 0;
#         int right = length - 1;
#         int current = length - 1;
#         vector<int> result(length, 0);
#         while (left <= right){
#             int L = A[left] * A[left];
#             int R = A[right] * A[right];
#             if (L <= R){
#                 result[current] = R;
#                 right -= 1;
#                 current -= 1;
#             }
#             else{
#                 result[current] = L;
#                 left += 1;
#                 current -= 1;
#             }
#         }
#         return result;
#     }
# };
        

