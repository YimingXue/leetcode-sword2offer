#
# @lc app=leetcode.cn id=938 lang=python
#
# [938] 最大为 N 的数字组合
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root == None:
            return 0
        if root.val > R:
            return self.rangeSumBST(root.left, L, R)
        elif root.val < L:
            return self.rangeSumBST(root.right, L, R)
        else:
            return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)

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
#     int rangeSumBST(TreeNode* root, int L, int R) {
#         if (!root) return 0;
#         int left_val, right_val;
#         if (root->val > R) return rangeSumBST(root->left, L, R);
#         else if (root->val < L) return rangeSumBST(root->right, L, R);
#         else return root->val + rangeSumBST(root->left, L, R) + rangeSumBST(root->right, L, R);
#     }
# };
