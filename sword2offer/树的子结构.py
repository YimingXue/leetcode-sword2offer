# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        # 空树不是任意一个树的子结构
        if not pRoot2:
            return False
        if not pRoot1:
            return False
        if pRoot1.val == pRoot2.val:
            if self.subtree(pRoot1, pRoot2):
                return True
            else:
                return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
        else:
            return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
    
    def subtree(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        elif not pRoot1 or pRoot1.val != pRoot2.val:
            return False
        else:
            return self.subtree(pRoot1.left, pRoot2.left) and self.subtree(pRoot1.right, pRoot2.right)