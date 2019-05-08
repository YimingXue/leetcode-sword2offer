# -*- coding:utf-8 -*-
# from collections import deque

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput) or k <= 0:
            return []
        
        heap = tinput[:k]
        # heap = deque(heap)
        # heap.appendleft(0)
        heap.insert(0, 0)
        len_heap = len(heap)-1
        adjust_first_num = len_heap // 2
        for i in range(adjust_first_num):
            self.adjust_heap(heap, adjust_first_num-i, len_heap)
        
        for i in range(k, len(tinput)):
            if tinput[i] < heap[1]:
                heap[1] = tinput[i]
                self.adjust_heap(heap, 1, len_heap)
        return sorted([heap[i] for i in range(1, len(heap))])
    
    def adjust_heap(self, tinput, start, end):
        temp = tinput[start]
        i = start
        j = 2 * i
        while j <= end:
            if j+1 <= end and tinput[j+1] > tinput[j]:
                j += 1
            if tinput[j] > temp:
                tinput[i] = tinput[j]
                i = j
                j = 2 * i
            else:
                break
        tinput[i] = temp
        return tinput

# # C++写法
# class Solution {
# public:
#     vector<int> GetLeastNumbers_Solution(vector<int> input, int k) {
#         vector<int> result;
#         if (k>input.size() || k<=0) return result;
        
#         vector<int> heap(input.begin(), input.begin()+k);
#         heap.insert(heap.begin(), 0);
#         int len_heap = heap.size()-1;
#         int first_adjust_num = len_heap / 2;
#         for (int i=0; i<first_adjust_num; i++){
#             heap = adjust_heap(heap, first_adjust_num-i, len_heap);
#         }
#         for (int i=k; i<input.size(); i++){
#             if (input[i] < heap[1]) {
#                 heap[1] = input[i];
#                 heap = adjust_heap(heap, 1, len_heap);
#             }
#         }
#         for (int i=heap.size()-1; i>=1; i--){
#             int temp = heap[1];
#             heap[1] = heap[i];
#             heap[i] = temp;
#             heap = adjust_heap(heap, 1, i-1);
#         }
#         result.assign(heap.begin()+1, heap.end());
#         return result;
#     }
    
#     vector<int> adjust_heap(vector<int> heap, int start, int end){
#         int temp = heap[start];
#         int i = start;
#         int j = 2 * i;
#         while (j<=end){
#             if (j+1<=end && heap[j+1]>heap[j]) j+= 1;
#             if (heap[j]>temp){
#                 heap[i] = heap[j];
#                 i = j;
#                 j = 2 * i;
#             }
#             else break;
#         }
#         heap[i] = temp;
#         return heap;
#     }
# };

if __name__ == '__main__':
    tinput = [4,5,1,6,2,7,2,8]
    print(Solution().GetLeastNumbers_Solution(tinput, 4))