#
# @lc app=leetcode.cn id=389 lang=python
#
# [389] 找不同
#
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = sorted(list(s))
        t = sorted(list(t))
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]

# class Solution {
# public:
#     char findTheDifference(string s, string t) {
#         char result;
#         int sum = 0;
#         for (int i = 0; i < s.size(); i++){
#             sum -= s[i];
#             sum += t[i];
#         }
#         sum += t[t.size()-1];
#         result = (char)sum;
#         return result;
#     }
# };
        

