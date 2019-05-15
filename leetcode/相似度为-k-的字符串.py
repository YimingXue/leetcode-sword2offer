#
# @lc app=leetcode.cn id=884 lang=python
#
# [884] 相似度为 K 的字符串
#
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        A = A.split(' ')
        B = B.split(' ')
        dictA = {}
        for item in A:
            dictA[item] = dictA.get(item, 0) + 1
        for item in B:
            dictA[item] = dictA.get(item, 0) + 1
        result = list()
        for key, value in dictA.items():
            if value == 1:
                result.append(key)
        return result

# # C++写法
# class Solution {
# public:
#     vector<string> uncommonFromSentences(string A, string B) {
#         unordered_map<string, int> m1;
#         vector<string> res;
#         int i = 0, j = 0;
#         while (j <= A.size()){
#             if (A[j] == ' ' || A[j] == '\0'){
#                 m1[A.substr(i, j-i)]++;
#                 i = j + 1;
#             }
#             j ++;
#         }
#         i = 0, j = 0;
#         while(j <= B.size()){
#             if (B[j] == ' ' || B[j] == '\0'){
#                 m1[B.substr(i, j-i)]++;
#                 i = j + 1;
#             }
#             j ++;
#         }
#         for (auto iter = m1.begin(); iter != m1.end(); iter++){
#             cout << iter->first << endl;
#             if (iter->second == 1)
#                 res.push_back(iter->first);
#         }
#         return res;
#     }
# };
        

