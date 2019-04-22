#
# @lc app=leetcode.cn id=744 lang=python
#
# [744] 网络延迟时间
#
# https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/description/
#
# algorithms
# Easy (42.22%)
# Total Accepted:    4K
# Total Submissions: 9.6K
# Testcase Example:  '["c","f","j"]\n"a"'
#
# 给定一个只包含小写字母的有序数组letters 和一个目标字母 target，寻找有序数组里面比目标字母大的最小字母。
# 
# 数组里字母的顺序是循环的。举个例子，如果目标字母target = 'z' 并且有序数组为 letters = ['a', 'b']，则答案返回 'a'。
# 
# 示例:
# 
# 
# 输入:
# letters = ["c", "f", "j"]
# target = "a"
# 输出: "c"
# 
# 输入:
# letters = ["c", "f", "j"]
# target = "c"
# 输出: "f"
# 
# 输入:
# letters = ["c", "f", "j"]
# target = "d"
# 输出: "f"
# 
# 输入:
# letters = ["c", "f", "j"]
# target = "g"
# 输出: "j"
# 
# 输入:
# letters = ["c", "f", "j"]
# target = "j"
# 输出: "c"
# 
# 输入:
# letters = ["c", "f", "j"]
# target = "k"
# 输出: "c"
# 
# 
# 注:
# 
# 
# letters长度范围在[2, 10000]区间内。
# letters 仅由小写字母组成，最少包含两个不同的字母。
# 目标字母target 是一个小写字母。
# 
# 
#
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # # 一次遍历
        # for item in letters:
        #     if item > target:
        #         return item
        # return letters[0]
        
        # 二分法
        low = 1
        high = len(letters)-1
        while low <= high:
            mid = (low + high) // 2
            if letters[mid-1] <= target and target < letters[mid]:
                return letters[mid]
            elif letters[mid-1] > target:
                high = mid - 1
            else:
                low = mid + 1
        return letters[0]

# # C++写法
# class Solution {
# public:
#     char nextGreatestLetter(vector<char>& letters, char target) {
#         int low = 1; int high = letters.size()-1;
#         int mid;
#         while (low <= high)
#         {
#             mid = (low + high) / 2;
#             if (letters[mid-1] <= target && letters[mid] > target) return letters[mid];
#             else if (letters[mid-1] > target) high = mid-1;
#             else low = mid+1;
#         }
#         return letters[0];
#     }
# };
        

