#
# @lc app=leetcode.cn id=94 lang=python
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (64.76%)
# Total Accepted:    27.1K
# Total Submissions: 41.8K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的中序 遍历。
# 
# 示例:
# 
# 输入: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# 输出: [1,3,2]
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 使用栈来存储遍历过的节点
        # 一路向左节点遍历并存在栈中，遇到空节点时pop出当父节点把值存在result中并指向右节点
        # 重复上述过程直至栈或者节点为空
        if not root:
            return []
        node = root
        result = list()
        stack = list()
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result

# C++解法
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
#     vector<int> inorderTraversal(TreeNode* root) {
#         vector<int> result;
#         if (root == NULL)
#             return result;
#         stack<TreeNode*> stack;
#         TreeNode* node(root);
#         while (!stack.empty() || node){
#             while (node){
#                 stack.push(node);
#                 node = node->left;
#             }
#             node = stack.top(); stack.pop();
#             result.push_back(node->val);
#             node = node->right;
#         }
#         return result;
#     }
# };
        

