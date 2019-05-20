#
# @lc app=leetcode.cn id=290 lang=python
#
# [290] 单词模式
#
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # split_str = str.split(' ')
        # if len(pattern) != len(split_str):
        #     return False
        # return len(set(zip(split_str, list(pattern)))) == len(set(pattern)) == len(set(split_str))
        
        pattern = list(pattern)
        str = str.split(' ')
        
        if len(pattern) != len(str):
            return False
        
        dict = {}
        for i in range(len(pattern)):
            if pattern[i] not in dict.keys():
                if str[i] in dict.values():
                    return False
                dict[pattern[i]] = str[i]
            else:
                if dict[pattern[i]] != str[i]:
                    return False
        return True

# # C++写法
# class Solution {
# public:
#     bool wordPattern(string pattern, string str) {
#         map<string, char> dict;
#         vector<string> str_vector;
        
#         // int i = 0, j = 0;
#         // while (j <= str.size()){
#         //     if (str[j] == ' ' || str[j] == '\0'){
#         //         str_vector.push_back(str.substr(i, j-i));
#         //         i = j + 1;
#         //     }
#         //     j ++;
#         // }
#         istringstream in(str);
#         string word;
#         while (in >> word){
#             str_vector.push_back(word);
#         }
        
#         if (pattern.size() != str_vector.size()) return false;
#         for (int i = 0; i < pattern.size(); i++){
#             if (dict.count(str_vector[i]) == 0){
#                 for (auto iter = dict.begin(); iter != dict.end(); iter++){
#                     if (iter->second == pattern[i]) return false;
#                 }
#                 dict[str_vector[i]] = pattern[i];
#             }
#             else{
#                 if (dict[str_vector[i]] != pattern[i]) return false;
#             }
#         }
#         return true;
#     }
# };
        

