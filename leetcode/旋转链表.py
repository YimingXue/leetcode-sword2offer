#
# @lc app=leetcode.cn id=61 lang=python
#
# [61] 旋转链表
#
# https://leetcode-cn.com/problems/rotate-list/description/
#
# algorithms
# Medium (37.55%)
# Total Accepted:    12.4K
# Total Submissions: 33.1K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
# 
# 示例 1:
# 
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
# 
# 
# 示例 2:
# 
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        p_head = head
        p_end = head; p_temp = head
        # 计算链表长度length，令k对length取余防止k大于链表长度
        length = 1
        node = head
        while node.next:
            node = node.next
            length += 1
        k = k % length
        if k == 0:
            return head
        # 使用双指针找到需要向右移动的起始节点位置
        for i in range(k):
            p_temp = p_temp.next
        while p_temp.next:
            p_temp = p_temp.next
            p_end = p_end.next
        # p_new_head是新的起始位置
        p_new_head = p_end.next
        # 找到以p_new_head为起始位置的链表末端并连接到p_head上
        node = p_new_head
        while node.next:
            node = node.next
        node.next = p_head
        # 最后将p_end.next置为None即可
        p_end.next = None
        return p_new_head
        

