# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = list()
        self.minstack = list()
        self.minnumber = float('inf')
    def push(self, node):
        # write code here
        self.stack.append(node)
        if node < self.minnumber:
            self.minstack.append(node)
            self.minnumber = node
        else:
            self.minstack.append(self.minnumber)
    def pop(self):
        # write code here
        self.minstack.pop()
        return self.stack.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.minstack[-1]