#
# @lc app=leetcode.cn id=173 lang=python
#
# [173] 二叉搜索树迭代器
#
# https://leetcode-cn.com/problems/binary-search-tree-iterator/description/
#
# algorithms
# Medium (59.36%)
# Total Accepted:    3.6K
# Total Submissions: 6.1K
# Testcase Example:  '["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]\n[[[7,3,15,null,null,9,20]],[null],[null],[null],[null],[null],[null],[null],[null],[null]]'
#
# 实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。
# 
# 调用 next() 将返回二叉搜索树中的下一个最小的数。
# 
# 
# 
# 示例：
# 
# 
# 
# BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // 返回 3
# iterator.next();    // 返回 7
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 9
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 15
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 20
# iterator.hasNext(); // 返回 false
# 
# 
# 
# 提示：
# 
# 
# next() 和 hasNext() 操作的时间复杂度是 O(1)，并使用 O(h) 内存，其中 h 是树的高度。
# 你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 中至少存在一个下一个最小的数。
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = list()
        self.find_left_most(root)
        
    def find_left_most(self, root):
        if not root:
            return 
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        node = self.stack.pop()
        self.find_left_most(node.right)
        return node.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# C++解法
# include<stack>

# struct TreeNode {
#     int val;
#     TreeNode* left;
#     TreeNode* right;
#     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
# }

# class BSTIterator{
# public:
#     stack<TreeNode*> s;

#     BSTIterator(TreeNode* root){

#     }

#     void find_left_most(TreeNode* root){
#         if (!root) return;
#         while (root){
#             s.push(root);
#             root = root.left;
#         }
#     }

#     int next(){
#         TreeNode* node = s.top();
#         s.pop();
#         find_left_most(node->right);
#         return node->val;
#     }

#     bool hasNext(){
#         return !s.empty();
#     }
# };