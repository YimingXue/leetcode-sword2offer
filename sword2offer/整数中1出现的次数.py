# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        for i in range(n+1):
            count += str(i).count('1')
        return count

if __name__ == '__main__':
    print(Solution().NumberOf1Between1AndN_Solution(300))