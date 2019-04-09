#
# @lc app=leetcode.cn id=79 lang=python
#
# [79] 单词搜索
#
# https://leetcode-cn.com/problems/word-search/description/
#
# algorithms
# Medium (36.40%)
# Total Accepted:    8.1K
# Total Submissions: 22.3K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
# 
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
# 
# 示例:
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# 给定 word = "ABCCED", 返回 true.
# 给定 word = "SEE", 返回 true.
# 给定 word = "ABCB", 返回 false.
# 
#
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.row = len(board)
        self.column = len(board[0])
        self.word = word
        self.board = board
        if len(board) == 0 or len(board[0]) == 0:
            return False
        for i in range(self.row):
            for j in range(self.column):
                if self.searcher(i, j, 0):
                    return True
        return False
    
    def searcher(self, i, j, index):
        if i == self.row or i < 0 or j == self.column or j < 0 or self.board[i][j] != self.word[index]:
            return False
        elif index == len(self.word) - 1:
            return True
        else:
            temp = self.board[i][j]
            self.board[i][j] = 0
            search = self.searcher(i+1, j, index+1) or self.searcher(i, j+1, index+1) or self.searcher(i-1, j, index+1) or self.searcher(i, j-1, index+1)
            self.board[i][j] = temp
            return search
        
        

if __name__ == '__main__':
#     board =[
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']]
#     word = "ABCCED"
    board = [["a","a"]]
    word = "aaa"
    print(Solution().exist(board, word))
        

