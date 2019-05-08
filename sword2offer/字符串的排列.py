# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        result = self.per(ss)
        return sorted(list(set(result)))

    def per(self, ss):
        if len(ss) < 1:
            return []
        if len(ss) == 1:
            return [ss]
        result = list()
        for i in range(len(ss)):
            for item in self.Permutation(ss[:i] + ss[i+1:]):
                result.append(ss[i]+item)
        return result