#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
#
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
#         self.n = n
#         self.result = list()
#         self.generate('', 0, 0)
#         return self.result
        
        
#     def generate(self, string, left, right):
#         if len(string) == self.n * 2:
#             self.result.append(string)
#             return 
#         if left >= self.n:
#             self.generate(string + ')', left, right + 1)
#         elif left >= right:
#             self.generate(string + '(', left + 1, right)
#             self.generate(string + ')', left, right + 1)
#         return 
        
        self.n = n
        self.result = list()
        self.generate('', 0, 0)
        return self.result
    
    def generate(self, string, left, right):
        if left > self.n or right > self.n or left < right:
            return
        elif len(string) == self.n * 2:
            self.result.append(string)
            return
        self.generate(string+'(', left + 1, right)
        self.generate(string+')', left, right + 1)
        return

# # C++写法
# class Solution {
# public:
#     vector<string> generateParenthesis(int n) {
#         vector<string> result;
#         generate(result, "", 0, 0, n);
#         return result;
#     }
    
#     void generate(vector<string>& result, string s, int left, int right, int n){
#         if (left > n || right > n || left < right) return;
#         else if (s.size() == n * 2){
#             result.push_back(s);
#             return;
#         }
#         generate(result, s+'(', left + 1, right, n);
#         generate(result, s+')', left, right + 1, n);
#         return;
#     }
# };
        

