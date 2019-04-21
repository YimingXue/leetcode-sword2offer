# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return pHead
        
        pHead = self.CloneListNode(pHead)
        pHead = self.CloneRandom(pHead)
        pHead, pHead_new = self.SeperateList(pHead)
        return pHead_new
    
    def CloneListNode(self, pHead):
        node = pHead
        while node:
            node_new = RandomListNode(node.label)
            temp = node.next
            node.next = node_new
            node_new.next = temp
            node = temp
        return pHead
    
    def CloneRandom(self, pHead):
        node = pHead
        while node:
            if node.random:
                node_new = node.next
                node_new.random = node.random.next
                node = node_new.next
            else:
                node = node.next
        return pHead
    
    def SeperateList(self, pHead):
        pHead_new = pHead.next
        node = pHead; node_new = pHead_new
        while node:
            node.next = node_new.next; node = node.next
            if node:
                node_new.next = node.next; node_new = node_new.next
        return pHead, pHead_new
    
    def display(self, pHead):
        node = pHead
        while node:
            print(node.label)
            node = node.next

    def display_random(self, pHead):
        node = pHead
        while node:
            if node.random:
                print(node.label, node.random.label)
                node = node.next
            else:
                node = node.next

if __name__ == "__main__":
    node1 = RandomListNode(1); node2 = RandomListNode(2); node3 = RandomListNode(3); node4 = RandomListNode(4); node5 = RandomListNode(5)
    node1.next = node2; node2.next = node3; node3.next = node4; node4.next = node5
    node1.random = node3; node2.random = node5; node4.random = node2
    pHead = node1
    Solution().Clone(pHead)

# # C++解法
# /*
# struct RandomListNode {
#     int label;
#     struct RandomListNode *next, *random;
#     RandomListNode(int x) :
#             label(x), next(NULL), random(NULL) {
#     }
# };
# */
# class Solution {
# public:
#     RandomListNode* Clone(RandomListNode* pHead)
#     {
#         if (!pHead) return pHead;
#         pHead = CloneListNode(pHead);
#         pHead = CloneRandom(pHead);
#         RandomListNode* pHead_new = Seperate(pHead);
#         return pHead_new;
#     }
#     RandomListNode* CloneListNode(RandomListNode* pHead)
#     {
#         RandomListNode* node = pHead;
#         while (node)
#         {
#             RandomListNode* node_new = new RandomListNode(node->label);
#             RandomListNode* temp = node->next;
#             node->next = node_new;
#             node_new->next = temp;
#             node = temp;
#         }
#         return pHead;
#     }
#     RandomListNode* CloneRandom(RandomListNode* pHead)
#     {
#         RandomListNode* node = pHead;
#         while (node)
#         {
#             if (node->random)
#             {
#                 RandomListNode* node_new = node->next;
#                 node_new->random = node->random->next;
#                 node = node_new->next;
#             }
#             else{
#                 node = node->next;
#             }
#         }
#         return pHead;
#     }
#     RandomListNode* Seperate(RandomListNode* pHead)
#     {
#         RandomListNode* pHead_new = pHead->next;
#         RandomListNode* node = pHead;
#         RandomListNode* node_new = pHead_new;
#         while (node)
#         {
#             node->next = node_new->next;
#             node = node->next;
#             if (node)
#             {
#                 node_new->next = node->next;
#                 node_new = node_new->next;
#             }
#         }
#         return pHead_new;
#     }
# };
    