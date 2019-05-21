#
# @lc app=leetcode.cn id=17 lang=python
#
# [17] 电话号码的字母组合
#
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.dict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        self.result = list()
        self.digits = digits
        if self.digits == None or len(self.digits) == 0:
            return self.result
        self.combinations('', 0)
        return self.result
        
    def combinations(self, string, k):
        if len(string) == len(self.digits):
            self.result.append(string)
            return
        temp = list(self.dict[self.digits[k]])
        for item in temp:
            string += item
            self.combinations(string, k+1)
            string = string[:-1]
        return

# # C++写法
# class Solution {
# public:
#     vector<string> letterCombinations(string digits) {
#         unordered_map<char, string> table{
#             {'0', " "}, {'1', "*"}, {'2', "abc"},
#             {'3', "def"}, {'4', "ghi"}, {'5', "jkl"},
#             {'6', "mno"}, {'7', "pqrs"}, {'8', "tuv"},
#             {'9', "wxyz"}};
#         vector<string> res;
#         if (digits == "") return res;
#         func(res, "", digits, table, 0);
#         return res;
#     }
    
#     void func(vector<string> &res, string str, string &digits, unordered_map<char, string> &m, int k){
#         if (str.size() == digits.size()){
#             res.push_back(str);
#             return;
#         }
#         string tmp = m[digits[k]];
#         for (char w : tmp){
#             str += w;
#             func(res, str, digits, m, k+1);
#             str.pop_back();
#         }
#         return;
#     }
# };
        

