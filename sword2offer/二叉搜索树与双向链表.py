# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        root = pRootOfTree
        if not root:
            return None
        if not root.left and not root.right:
            return root
        # 先处理左子树，将根节点和左子树中最大的节点相连
        self.Convert(root.left)
        left = root.left
        if left:
            while left.right:
                left = left.right
            root.left = left
            left.right = root
        # 处理右子树，将根节点和右子树中最小的节点相连
        self.Convert(root.right)
        right = root.right
        if right:
            while right.left:
                right = right.left
            root.right = right
            right.left = root
        # 找到头结点并返回
        while root.left:
            root = root.left
        return root

# # C++写法
# /*
# struct TreeNode {
# 	int val;
# 	struct TreeNode *left;
# 	struct TreeNode *right;
# 	TreeNode(int x) :
# 			val(x), left(NULL), right(NULL) {
# 	}
# };*/
# class Solution {
# public:
#     TreeNode* Convert(TreeNode* pRootOfTree)
#     {
#         TreeNode* root = pRootOfTree;
#         if (!root) return root;
#         if (!root->left && !root->right) return root;
#         Convert(root->left);
#         TreeNode* left = root->left;
#         if (left)
#         {
#             while (left->right) left = left->right;
#             root->left = left; left->right = root;
#         }
#         Convert(root->right);
#         TreeNode* right = root->right;
#         if (right)
#         {
#             while (right->left) right = right->left;
#             root->right = right; right->left = root;
#         }
#         while (root->left) root = root->left;
#         return root;
#     }
# };