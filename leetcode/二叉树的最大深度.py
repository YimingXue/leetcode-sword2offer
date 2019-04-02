# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 递归遍历二叉树，返回左子树和右子树深度的最大值，遇到空节点返回0即可
        if not root:
            return 0
        depth_left = self.maxDepth(root.left) + 1
        depth_right = self.maxDepth(root.right) + 1
        return max(depth_left, depth_right)
        