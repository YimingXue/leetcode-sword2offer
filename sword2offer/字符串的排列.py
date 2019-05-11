# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        result = self.per(ss)
        return sorted(list(set(result)))

    def per(self, ss):
        if len(ss) < 1:
            return []
        if len(ss) == 1:
            return [ss]
        result = list()
        for i in range(len(ss)):
            for item in self.Permutation(ss[:i] + ss[i+1:]):
                result.append(ss[i]+item)
        return result

# # C++写法
# #include <algorithm>

# class Solution {
# public:
#     vector<string> Permutation(string str) {
#         vector<string> result = per(str);
#         std::sort(result.begin(), result.end());
#         result.erase(std::unique(result.begin(), result.end()), result.end());
#         return result;
#     }
    
#     vector<string> per(string str){
#         vector<string> result_temp;
#         if (str.size()<1) return result_temp;
#         if (str.size()==1){
#             result_temp.push_back(str);
#             return result_temp;
#         }
#         vector<string> result;
#         for (int i=0; i<str.size(); i++){
#             vector<string> temp = Permutation(str.substr(0,i)+str.substr(i+1));
#             for (auto item : temp){
#                 result.push_back(str[i]+item);
#             }
#         }
#         return result;
#     }
# };