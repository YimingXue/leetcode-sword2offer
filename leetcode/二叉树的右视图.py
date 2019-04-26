#
# @lc app=leetcode.cn id=199 lang=python
#
# [199] 二叉树的右视图
#
# https://leetcode-cn.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (56.67%)
# Total Accepted:    4.5K
# Total Submissions: 7.9K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
# 
# 示例:
# 
# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
# 
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            nodes = []
            nodesValue = []
            for node in queue:
                nodesValue.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            result.append(nodesValue[-1])
            queue = nodes
        return result

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
#     vector<int> rightSideView(TreeNode* root) {
#         vector<int> result;
#         vector<TreeNode*> queue{root};
#         if (!root) return result;
#         while (queue.size() != 0)
#         {
#             vector<TreeNode*> nodes;
#             vector<int> nodesValue;
#             for (int i=0; i<queue.size(); i++)
#             {
#                 nodesValue.push_back(queue[i]->val);
#                 if (queue[i]->left) nodes.push_back(queue[i]->left);
#                 if (queue[i]->right) nodes.push_back(queue[i]->right);
#             }
#             result.push_back(nodesValue[nodesValue.size()-1]);
#             queue = nodes;
#         }
#         return result;
#     }
# };
        

