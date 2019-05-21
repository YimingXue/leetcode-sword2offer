#
# @lc app=leetcode.cn id=844 lang=python
#
# [844] Backspace String Compare
#
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = list()
        for item in list(S):
            if item == '#':
                if len(s) != 0:
                    s.pop()
                else:
                    continue
            else: s.append(item)
        t = list()
        for item in list(T):
            if item == '#':
                if len(t) != 0:
                    t.pop()
                else:
                    continue
            else: t.append(item)
        return True if s == t else False

# # C++写法
# class Solution {
# public:
#     bool backspaceCompare(string S, string T) {
#         string s, t;
#         for (char item : S){
#             if (item == '#'){
#                 if (s.size() != 0) s.pop_back();
#                 else continue;
#             }
#             else s.push_back(item);
#         }
#         for (char item : T){
#             if (item == '#'){
#                 if (t.size() != 0) t.pop_back();
#                 else continue;
#             }
#             else t.push_back(item);
#         }
#         if (s == t) return true;
#         else return false;
#     }
# };
        

