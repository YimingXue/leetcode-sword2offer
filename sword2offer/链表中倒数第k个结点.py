# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        record = list()
        while head:
            record.append(head)
            head = head.next
        if k <= 0 or k > len(record):
            return None
        return record[-k]

    def FindKthToTail_function2(self, head, k):
        # write code here
        if not head:
            return None
        left = head
        right = head
        for i in range(k):
            if not right:
                return None
            right = right.next
        while right:
            left = left.next
            right = right.next
        return left