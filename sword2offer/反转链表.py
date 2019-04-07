# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        pre = None
        node = pHead
        while node:
            temp = node.next
            node.next = pre
            pre = node
            node = temp
        return pre