#
# @lc app=leetcode.cn id=64 lang=python
#
# [64] 最小路径和
#
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[m-1][n-1]

# # C++写法
# class Solution {
# public:
#     int minPathSum(vector<vector<int>>& grid) {
#         if (grid.size() == 0 || grid[0].size() == 0) return 0;
#         int m = grid.size();
#         int n = grid[0].size();
#         for (int i = 1; i < m; i++) grid[i][0] += grid[i-1][0];
#         for (int j = 1; j < n; j++) grid[0][j] += grid[0][j-1];
#         for (int i = 1; i < m; i++){
#             for (int j = 1; j < n; j++){
#                 grid[i][j] += min(grid[i-1][j], grid[i][j-1]);
#             }
#         }
#         return grid[m-1][n-1];
#     }
# };
        

