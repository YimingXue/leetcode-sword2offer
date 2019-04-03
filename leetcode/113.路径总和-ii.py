#
# @lc app=leetcode.cn id=113 lang=python
#
# [113] 路径总和 II
#
# https://leetcode-cn.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (53.40%)
# Total Accepted:    7.1K
# Total Submissions: 13.3K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
# 
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \    / \
# ⁠       7    2  5   1
# 
# 
# 返回:
# 
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
# ]
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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        # 递归实现，从根节点开始向下递归，每次减去当前节点数值，如果到叶子节点时数值为零则保存在全局变量result中
        self.sum = sum
        if not root:
            return []
        self.result = []
        self.path_recursion(root, sum, [])
        return self.result

    def path_recursion(self, root, currentValue, path):
        temp_path = path[:]
        if not root:
            return 
        if not root.left and not root.right and (currentValue-root.val) == 0:
            temp_path.append(root.val)
            self.result.append(temp_path)
            return 
        else:
            temp_path.append(root.val)
        
        self.path_recursion(root.left, currentValue-root.val, temp_path)
        self.path_recursion(root.right, currentValue-root.val, temp_path)
        

