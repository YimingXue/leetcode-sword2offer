#
# @lc app=leetcode.cn id=278 lang=python
#
# [278] 第一个错误的版本
#
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        while low <= high:
            mid = (low + high) / 2
            if mid-1>=0 and isBadVersion(mid)==True and isBadVersion(mid-1)==False:
                return mid
            elif isBadVersion(mid) == True:
                high = mid
            elif isBadVersion(mid) == False:
                low = mid + 1
        return -1

# # C++写法
# // Forward declaration of isBadVersion API.
# bool isBadVersion(int version);

# class Solution {
# public:
#     int firstBadVersion(int n) {
#         int low = 1;
#         int high = n;
#         while (low <= high){
#             int mid = low + (high-low) / 2; # 注意这里的写法，如果(int mid = (low+high)/2)会报错，两个大整数相加超出int类型范围，因此用这种写法会更好！！！
#             if (mid-1>=0 && isBadVersion(mid)==true && isBadVersion(mid-1)==false) return mid;
#             else if (isBadVersion(mid)==true) high = mid;
#             else if (isBadVersion(mid)==false) low = mid + 1;
#         }
#         return -1;
#     }
# };
        

