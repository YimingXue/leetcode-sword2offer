# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        root = None
        return self.reconstruct(root, pre, tin)
        
    def reconstruct(self, root, pre, tin):
        if len(pre) == 0 and len(tin) == 0:
            root = None
            return
        root_value = pre[0]
        root = TreeNode(root_value)
        index_tin = tin.index(root_value)
        len_left = index_tin
        root.left = self.reconstruct(root.left, pre[1:len_left+1], tin[0:len_left])
        root.right = self.reconstruct(root.right, pre[len_left+1:len(pre)], tin[len_left+1:len(tin)])
        return root
    
    # 写个前序遍历，用于检查结果是否正确
    def preTraverse_stack(self, root):
        if not root:
            return []
        result = list()
        stack = list()
        node = root
        while stack or node:
            while node:
                stack.append(node)
                result.append(node.val)
                node = node.left
            node = stack.pop()
            node = node.right
        return result

if __name__ == "__main__":
    pre = [1,2,4,7,3,5,6,8]
    tin = [4,7,2,1,5,3,8,6]
    root = Solution().reConstructBinaryTree(pre, tin)
    print(Solution().preTraverse_stack(root))
    