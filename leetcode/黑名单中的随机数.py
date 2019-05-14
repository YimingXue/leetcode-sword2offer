#
# @lc app=leetcode.cn id=894 lang=python
#
# [894] 黑名单中的随机数
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0: return []
        if N == 1: return [TreeNode(0)]
        res = list()
        for i in range(1, N, 2):
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(N-i-1):
                    node = TreeNode(0)
                    node.left = left
                    node.right = right
                    res.append(node)
        return res
        
# # C++写法
# /**
#  * Definition for a binary tree node.
#  * struct TreeNode {
#  *     int val;
#  *     TreeNode *left;
#  *     TreeNode *right;
#  *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
#  * };
#  */
# class Solution {
# public:
#     vector<TreeNode*> allPossibleFBT(int N) {
#         vector<TreeNode*> res;
#         if (N % 2 == 0) {
#             return res;
#         }
#         if (N == 1){
#             TreeNode* node = new TreeNode(0);
#             res.push_back(node);
#         }
#         for (int i = 1; i < N; i += 2){
#             vector<TreeNode*> left_vector = allPossibleFBT(i);
#             vector<TreeNode*> right_vector = allPossibleFBT(N-i-1);
#             for (TreeNode* left : left_vector){
#                 for (TreeNode* right : right_vector){
#                     TreeNode* node = new TreeNode(0);
#                     node->left = left;
#                     node->right = right;
#                     res.push_back(node);
#                 }
#             }
#         }
#         return res;
#     }
# };
