#
# @lc app=leetcode.cn id=206 lang=python
#
# [206] 反转链表
#
# https://leetcode-cn.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (59.63%)
# Total Accepted:    48.7K
# Total Submissions: 81.4K
# Testcase Example:  '[1,2,3,4,5]'
#
# 反转一个单链表。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # # 迭代方法
        # # 分别用到三个节点，node为当前节点，pre为node前一个节点（也是要连接的节点），temp为node后一个节点
        # # 之后分成三步，node.next = pre; pre = node; node = temp（因为node.next已经改变了）
        # # 这里需要注意的是返回的是pre而不是node
        # pre = None
        # node = head
        # while node:
        #     temp = node.next
        #     node.next = pre
        #     pre = node
        #     node = temp
        # return pre
        
        # 递归方法
        if not head:
            return head
        pre = None
        node = head
        return self.recursion(pre, node)
        
    def recursion(self, pre, node):
        if not node:
            return pre
        temp = node.next
        node.next = pre
        pre = node
        node = temp
        head = self.recursion(pre, node)
        return head
        

