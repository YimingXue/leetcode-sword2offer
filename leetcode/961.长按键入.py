#
# @lc app=leetcode.cn id=961 lang=python
#
# [961] 长按键入
#
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        while j < len(typed) and i < len(name):
            if typed[j] == name[i]:
                i += 1
                j += 1
            else:
                if i-1 >= 0 and typed[j] == name[i-1]:
                    j += 1
                else:
                    return False
        # if i <= len(name)-1: return False
        # if len(list(set(typed[j-1:]))) == 1: 
        #     return True
        # else:
        #     return False
        return i == len(name)

# # C++写法
# class Solution {
# public:
#     bool isLongPressedName(string name, string typed) {
#         int i = 0, j = 0;
#         while (i < name.size() && j < typed.size()){
#             if (name[i] == typed[j]){
#                 i += 1;
#                 j += 1;
#             }
#             else{
#                 if (typed[j] == name[i-1]){
#                     j += 1;
#                 }
#                 else{
#                     return false;
#                 }
#             }
#         }
#         if (i == name.size()) return true;
#         else return false;
#     }
# };
        

