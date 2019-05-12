#
# @lc app=leetcode.cn id=63 lang=python
#
# [63] 不同路径 II
#
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0;
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == 1 and n == 1 and obstacleGrid[0][0] == 1: return 0
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1
        
        for i in range(m):
            if obstacleGrid[i][0] == -1:
                break
            else:
                obstacleGrid[i][0] = 1
        for i in range(n):
            if obstacleGrid[0][i] == -1:
                break
            else:
                obstacleGrid[0][i] = 1
        # print(obstacleGrid)
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == -1:
                    continue
                if i-1 >= 0 and j-1 >= 0 and obstacleGrid[i-1][j] != -1 and obstacleGrid[i][j-1] != -1:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                elif i-1 >= 0 and obstacleGrid[i-1][j] != -1:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j]
                elif j-1 >= 0 and obstacleGrid[i][j-1] != -1:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1]
        # print(obstacleGrid)
        return obstacleGrid[m-1][n-1] if obstacleGrid[m-1][n-1] != -1 else 0

# # C++写法
# class Solution {
# public:
#     int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
#         if (obstacleGrid.size() == 0 || obstacleGrid[0].size() == 0) return 0;
#         if (obstacleGrid.size() == 1 && obstacleGrid[0].size() == 1 && obstacleGrid[0][0] == 0) return 1;
#         int m = obstacleGrid.size();
#         int n = obstacleGrid[0].size();
#         vector<vector<long>> temp(m, vector<long>(n,0));
#         for (int i = 0; i < m; i++){
#             for (int j = 0; j < n; j++){
#                 if (obstacleGrid[i][j] == 1) temp[i][j] = -1;
#             }
#         }
#         for (int i = 0; i < m; i++){
#             if (temp[i][0] == -1) break;
#             else temp[i][0] = 1;
#         }
#         for (int i = 0; i < n; i ++){
#             if (temp[0][i] == -1) break;
#             else temp[0][i] = 1;
#         }
        
#         for (int i = 0; i < m; i++){
#             for (int j = 0; j < n; j++){
#                 if (temp[i][j] == -1) continue;
#                 if (i-1 >= 0 && j-1 >= 0 && temp[i-1][j] != -1 and temp[i][j-1] != -1){
#                     temp[i][j] = temp[i-1][j] + temp[i][j-1];
#                 }
#                 else if (i-1 >= 0 && temp[i-1][j] != -1){
#                     temp[i][j] = temp[i-1][j];
#                 }
#                 else if (j-1 >= 0 && temp[i][j-1] != -1){
#                     temp[i][j] = temp[i][j-1];
#                 }
#             }
#         }
#         if (temp[m-1][n-1] == -1) return 0;
#         return temp[m-1][n-1];
#     }
# };

