#
# @lc app=leetcode.cn id=101 lang=python
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (45.79%)
# Total Accepted:    29.9K
# Total Submissions: 64.8K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
# 
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 说明:
# 
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def Symmetric(p, q):
            if p == None and q == None:
                return True
            if (p == None and q != None) or (p != None and q == None) or (p.val != q.val):
                return False
            else:
                pb = Symmetric(p.left, q.right)
                qb = Symmetric(p.right, q.left)
                return pb and qb
            
        p = root
        q = root
        return Symmetric(p, q)
        

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
#     bool isSymmetric(TreeNode* root) {
#         if (!root) return true;
#         return recursion(root->left, root->right);
#     }
    
#     bool recursion(TreeNode* root1, TreeNode* root2){
#         if (!root1 && !root2){
#             return true;
#         }
#         else if (root1 && root2 && root1->val == root2->val){
#             return recursion(root1->left, root2->right) && recursion(root1->right, root2->left);
#         }
#         else{
#             return false;
#         }
#     }
# };
