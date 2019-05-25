#
# @lc app=leetcode.cn id=203 lang=python
#
# [203] 移除链表元素
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return head
        while head.val == val:
            head = head.next
            if head == None:
                return head
        pre = head
        now = head.next
        while now != None:
            if now.val == val:
                pre.next = now.next
            else:
                pre = pre.next
            now = now.next
        return head

# # C++写法
# /**
#  * Definition for singly-linked list.
#  * struct ListNode {
#  *     int val;
#  *     ListNode *next;
#  *     ListNode(int x) : val(x), next(NULL) {}
#  * };
#  */
# class Solution {
# public:
#     ListNode* removeElements(ListNode* head, int val) {
#         if (!head) return head;
#         while (head->val == val){
#             head = head->next;
#             if (!head) return head;
#         } 
#         ListNode* node = head;
#         while (node->next){
#             if (node->next->val == val){
#                 node->next = node->next->next;
#             }
#             else{
#                 node = node->next;
#             }
#         }
#         return head;
#     }
# };
        

