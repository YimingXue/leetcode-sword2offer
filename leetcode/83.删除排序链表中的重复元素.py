#
# @lc app=leetcode.cn id=83 lang=python
#
# [83] 删除排序链表中的重复元素
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        node = head
        while node.next != None:
            if node.next.val == node.val:
                node.next = node.next.next
                continue
            node = node.next
        # while node.next != None:
        #     print node.val
        #     node = node.next
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
#     ListNode* deleteDuplicates(ListNode* head) {
#         if (!head) return head;
#         ListNode* node = head;
#         while (node->next){
#             if (node->next->val == node->val) node->next = node->next->next;
#             else node = node->next;
#         }
#         return head;
#     }
# };
        

