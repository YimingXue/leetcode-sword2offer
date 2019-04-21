# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        root = sequence[-1]
        i = 0
        for node in sequence[:-1]:
            if node <= root:
                i += 1
            else:
                break
        for node in sequence[i:-1]:
            if node < root:
                return False
        
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        right = True
        if i < len(sequence)-1 and right:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right

# # C++解法
# class Solution {
# public:
#     bool VerifySquenceOfBST(vector<int> sequence) {
#         if (sequence.size()==0) return false;
#         return recursion(sequence);
#     }
    
#     bool recursion(vector<int> sequence){
#         if (sequence.size() == 0) return true;
#         int split;
#         int value = sequence.back();
#         for (int i=0; i!=sequence.size()-1; i++){
#             if (sequence[i]>value){
#                 split = i;
#                 break;
#             }
#         }
#         for (int i=split; i!=sequence.size()-1; i++){
#             if (sequence[i]<value) return false;
#         }
#         vector<int> seqleft(sequence.begin(), sequence.begin()+split);
#         vector<int> seqright(sequence.begin()+split, sequence.end()-1);
#         return recursion(seqleft) && recursion(seqright);
#     }
# };