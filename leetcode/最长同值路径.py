#
# @lc app=leetcode.cn id=687 lang=python
#
# [687] 最长同值路径
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.maxLen = 0
        if not root:
            return 0
        self.longest(root, None)
        return self.maxLen
    
    def longest(self, root, rootVal):
        if not root:
            return 0
        leftLen = self.longest(root.left, root.val)
        rightLen = self.longest(root.right, root.val)
        self.maxLen = max(self.maxLen, leftLen + rightLen)
        if root.val == rootVal:
            return max(leftLen, rightLen) + 1
        else:
            return 0

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
#     int maxLen = 0;
#     int longestUnivaluePath(TreeNode* root) {
#         longest(root, NULL);
#         return this->maxLen;
#     }
    
#     int longest(TreeNode* root, int value){
#         if (!root) return 0;
#         int leftLen = longest(root->left, root->val);
#         int rightLen = longest(root->right, root->val);
#         this->maxLen = max(this->maxLen, leftLen + rightLen);
#         if (root->val == value){
#             return max(leftLen, rightLen) + 1;
#         }
#         return 0;
#     }
# };
        

