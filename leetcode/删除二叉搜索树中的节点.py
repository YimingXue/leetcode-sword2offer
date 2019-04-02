# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        # 解题思路分成两部分：查找目标节点，删除目标节点
        # 第一步使用递归寻找二叉搜索树中的目标值
        # 第二步会有三种情况，一种是目标节点没有左右孩子，则直接置为None即可
        #                   第二种是目标节点只有一个左右孩子，则直接将目标节点替换成左右孩子即可
        #                   第三种是目标节点既有左孩子也有右孩子，则要选取目标节点右孩子中最左边的节点作为目标节点的值，并将其置为None
        #                                                     因为该值为大于目标节点的最小的数值
        if root == None:
            return None
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left != None and root.right != None:
                temp = root.right
                while temp.left != None:
                    temp = temp.left
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)
            else:
                if root.left != None:
                    root = root.left
                elif root.right != None:
                    root = root.right
                else:
                    root = None
        return root