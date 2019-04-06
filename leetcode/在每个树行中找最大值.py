#
# @lc app=leetcode.cn id=515 lang=python
#
# [515] 在每个树行中找最大值
#
# https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/description/
#
# algorithms
# Medium (55.67%)
# Total Accepted:    2.1K
# Total Submissions: 3.8K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# 您需要在二叉树的每一行中找到最大的值。
# 
# 示例：
# 
# 
# 输入: 
# 
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      / \   \  
# ⁠     5   3   9 
# 
# 输出: [1, 3, 9]
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
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        node = root
        queue = [node]
        result = list()
        while queue:
            mx = queue[0].val
            nodes = list()
            for node in queue:
                if node.val >= mx:
                    mx = node.val
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            result.append(mx)
            queue = nodes
        return result
        

