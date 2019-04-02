# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        count = s.count(' ')
        new_length = len(s) + count * 2
        result = [0 for _ in range(new_length)]
        index_s = len(s) - 1
        index_result = new_length - 1
        while index_result >= 0:
            if s[index_s] == ' ':
                result[index_result-2:index_result+1] = ['%', '2', '0']
                index_result -= 3
                index_s -= 1
            else:
                result[index_result] = s[index_s]
                index_result -= 1
                index_s -= 1
        return ''.join(result)