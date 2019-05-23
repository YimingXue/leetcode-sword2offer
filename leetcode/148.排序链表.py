#
# @lc app=leetcode.cn id=148 lang=python
#
# [148] 排序链表
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head: return head
        return self.mergeSort(head)
        
    def mergeSort(self, head):
        if not head or not head.next: return head
        slow = head
        fast = head
        pre_slow = head
        while fast and fast.next:
            fast = fast.next.next
            pre_slow = slow
            slow = slow.next
        pre_slow.next = None
        l1 = self.mergeSort(head)
        l2 = self.mergeSort(slow)
        return self.merge(l1, l2)
    
    def merge(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        if l1.val <= l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l2.next, l1)
            return l2

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
#     ListNode* sortList(ListNode* head) {
#         return mergeSort(head);
#     }
    
#     ListNode* mergeSort(ListNode* node){
#         if (!node || !node->next) return node;
#         // 快慢指针
#         ListNode* fast = node;
#         ListNode* slow = node;
#         ListNode* breakN = node;
#         while (fast && fast-> next){
#             fast = fast->next->next;
#             breakN = slow;
#             slow = slow->next;
#         }
#         breakN->next = nullptr;
#         ListNode* l1 = mergeSort(node);
#         ListNode* l2 = mergeSort(slow);
#         return merge(l1, l2);
#     }
    
#     ListNode* merge(ListNode* l1, ListNode* l2){
#         // 递归到底的情况
#         if (l1 == nullptr) return l2;
#         if (l2 == nullptr) return l1;
#         // 分情况递归实现
#         if (l1->val <= l2->val){
#             l1->next = merge(l1->next, l2);
#             return l1;
#         } else {
#             l2->next = merge(l2->next, l1);
#             return l2;
#         }
#     }
# };
        

