# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        node = ListNode(None)
        head = node
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                node.next = ListNode(pHead1.val)
                pHead1 = pHead1.next
                node = node.next
            else:
                node.next = ListNode(pHead2.val)
                pHead2 = pHead2.next
                node = node.next
        if pHead1:
            node.next = pHead1
        else:
            node.next = pHead2
        return head.next