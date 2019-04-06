#
# @lc app=leetcode.cn id=623 lang=python
#
# [623] 在二叉树中增加一行
#
# https://leetcode-cn.com/problems/add-one-row-to-tree/description/
#
# algorithms
# Medium (45.82%)
# Total Accepted:    897
# Total Submissions: 1.9K
# Testcase Example:  '[4,2,6,3,1,5]\n1\n2'
#
# 给定一个二叉树，根节点为第1层，深度为 1。在其第 d 层追加一行值为 v 的节点。
# 
# 添加规则：给定一个深度值 d （正整数），针对深度为 d-1 层的每一非空节点 N，为 N 创建两个值为 v 的左子树和右子树。
# 
# 将 N 原先的左子树，连接为新节点 v 的左子树；将 N 原先的右子树，连接为新节点 v 的右子树。
# 
# 如果 d 的值为 1，深度 d - 1 不存在，则创建一个新的根节点 v，原先的整棵树将作为 v 的左子树。
# 
# 示例 1:
# 
# 
# 输入: 
# 二叉树如下所示:
# ⁠      4
# ⁠    /   \
# ⁠   2     6
# ⁠  / \   / 
# ⁠ 3   1 5   
# 
# v = 1
# 
# d = 2
# 
# 输出: 
# ⁠      4
# ⁠     / \
# ⁠    1   1
# ⁠   /     \
# ⁠  2       6
# ⁠ / \     / 
# ⁠3   1   5   
# 
# 
# 
# 示例 2:
# 
# 
# 输入: 
# 二叉树如下所示:
# ⁠     4
# ⁠    /   
# ⁠   2    
# ⁠  / \   
# ⁠ 3   1    
# 
# v = 1
# 
# d = 3
# 
# 输出: 
# ⁠     4
# ⁠    /   
# ⁠   2
# ⁠  / \    
# ⁠ 1   1
# ⁠/     \  
# 3       1
# 
# 
# 注意:
# 
# 
# 输入的深度值 d 的范围是：[1，二叉树最大深度 + 1]。
# 输入的二叉树至少有一个节点。
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
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            result = TreeNode(v)
            result.left = root
            return result
        node = root
        queue = [node]
        level = 0
        flag = False
        while queue and not flag:
            nodes = list()
            level += 1
            for node in queue:
                if level == d-1:
                    # 左子树
                    temp = TreeNode(v)
                    temp.left = node.left
                    node.left = temp
                    # 右子树
                    temp = TreeNode(v)
                    temp.right = node.right
                    node.right = temp
                    flag = True
                else:
                    if node.left:
                        nodes.append(node.left)
                    if node.right:
                        nodes.append(node.right)
            queue = nodes
        if not flag:
            result = TreeNode(v)
            result.left = root
            return result
        return root
        

