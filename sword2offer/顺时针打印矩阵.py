# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = list()
        while matrix:
            result.extend(matrix[0])
            if len(matrix[1:]) == 0:
                break
            matrix = self.rotate(matrix[1:])
        return result
    
    def rotate(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        temp = list()
        for i in range(col):
            temp.append([matrix[j][i] for j in range(row)])
        temp = temp[::-1]
        return temp