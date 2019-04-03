#
# @lc app=leetcode.cn id=513 lang=python
#
# [513] 找树左下角的值
#
# https://leetcode-cn.com/problems/find-bottom-left-tree-value/description/
#
# algorithms
# Medium (64.01%)
# Total Accepted:    2.6K
# Total Submissions: 4.1K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树，在树的最后一行找到最左边的值。
# 
# 示例 1:
# 
# 
# 输入:
# 
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 
# 输出:
# 1
# 
# 
# 
# 
# 示例 2: 
# 
# 
# 输入:
# 
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   5   6
# ⁠      /
# ⁠     7
# 
# 输出:
# 7
# 
# 
# 
# 
# 注意: 您可以假设树（即给定的根节点）不为 NULL。
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        node = root
        queue = [node]
        result = list()
        while queue:
            nodes = list()
            nodesvalue = list()
            for node in queue:
                nodesvalue.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            result.append(nodesvalue)
            queue = nodes
        return result[-1][0]

    def findBottomLeftValue_function2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        node = root
        queue = [node]
        result = root.val
        while queue:
            nodes = list()
            result = queue[0].val
            for node in queue:
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            if nodes:
                result = nodes[0].val
            queue = nodes
        return result

    def findBottomLeftValue_function3(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        for node in queue:
            queue += filter(None, (node.right, node.left))
        return node.val
     
    
     