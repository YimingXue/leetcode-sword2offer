# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        count = 0
        current = numbers[0]
        for item in numbers:
            if item == current:
                count += 1
            else:
                count -= 1
            if count == 0:
                count = 1
                current = item
        return current if numbers.count(current) > len(numbers)/2 else 0

# # C++写法
# #include <algorithm>
# class Solution {
# public:
#     int MoreThanHalfNum_Solution(vector<int> numbers) {
#         int count = 0;
#         int current = numbers[0];
#         for (int i=0; i<numbers.size(); i++){
#             if (numbers[i]==current) count += 1;
#             else count -= 1;
#             if (count==0){
#                 count = 1;
#                 current = numbers[i];
#             }
#         }
#         int count_current = 0;
#         for (int i=0; i<numbers.size(); i++){
#             if (numbers[i] == current){
#                 count_current += 1;
#             }
#         }
#         if (count_current > numbers.size()/2) return current;
#         else return 0;
#     }
# };