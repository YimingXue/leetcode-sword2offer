# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        self.result = list()
        self.path(root, expectNumber, [])
        return self.result
        
    def path(self, root, expectNumber, value_list):
        temp = value_list[:]
        temp.append(root.val)
        currentValue = expectNumber - root.val
        if not root.left and not root.right and currentValue == 0:
            self.result.append(temp)
            return 

        if root.left:
            self.path(root.left, currentValue, temp)
        if root.right:
            self.path(root.right, currentValue, temp)
        return 

# # C++解法
# /*
# struct TreeNode {
# 	int val;
# 	struct TreeNode *left;
# 	struct TreeNode *right;
# 	TreeNode(int x) :
# 			val(x), left(NULL), right(NULL) {
# 	}
# };*/
# class Solution {
# public:
#     vector<vector<int> > result;
#     vector<vector<int> > FindPath(TreeNode* root,int expectNumber) {
#         if (!root) return result;
#         vector<int> route;
#         path(root, route, expectNumber);
#         return this->result;
#     }
#     void path(TreeNode* root, vector<int> route, int expectNumber){
#         vector<int> temp(route);
#         temp.push_back(root->val);
#         int currentValue = expectNumber - root->val;
#         if (!root->left && !root->right && currentValue==0){
#             this->result.push_back(temp);
#             return;
#         }
#         if (root->left) path(root->left, temp, currentValue);
#         if (root->right) path(root->right, temp, currentValue);
#         return;
#     }
# };