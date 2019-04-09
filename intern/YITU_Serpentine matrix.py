# 蛇形矩阵的生成，输入一个数字N，比如为4，现场手写代码生成下面矩阵：
# 1  2  6  7
# 3  5  8  13
# 4  9  12 14
# 10 11 15 16

class Solution(object):
    def sprpentineMatrix(self, N):
        self.result = [[0 for _ in range(N)] for _ in range(N)]
        self.count = 1
        self.reverseFlag = True
        index_row = 0; index_col = 0
        while index_row < N:
            self.getMatrix(index_row, index_col)
            index_row += 1
        index_row -= 1; index_col += 1
        while index_col < N:
            self.getMatrix(index_row, index_col)
            index_col += 1
        return self.result
    
    def getMatrix(self, index_row, index_col):
        if self.reverseFlag:
            i = index_row; j = index_col
            while i >= index_col and j <= index_row:
                self.result[i][j] = self.count
                i -= 1; j += 1; self.count += 1
        else:
            i = index_col; j = index_row
            while i <= index_row and j >= index_col:
                self.result[i][j] = self.count
                i += 1; j -= 1; self.count += 1
        self.reverseFlag = not self.reverseFlag



if __name__ == '__main__':
    print(Solution().sprpentineMatrix(N=4))
