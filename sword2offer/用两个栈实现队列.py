# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()
    
    def push(self, node):
        # write code here
        self.stack1.append(node)
        
    def pop(self):
        # return xx
        if len(self.stack2) != 0:
            return self.stack2.pop()
        elif len(self.stack1) != 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            return None

if __name__ == '__main__':
    queue = Solution()
    queue.push(1)
    queue.push(3)
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())