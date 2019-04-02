# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # 和一般的旋转数组两部分都是严格递增的二分查找不太一样，这道题中的旋转数组是非严格递增的
        # 所以不能通过比较mid指向值和low指向值的大小来进行判断。
        # 使用mid指针和high指向值进行比较，如果mid指向值更大，则说明最小值存在于mid和high之间，且mid值不会是最小值，因此使low=mid+1
        # 如果mid指向值更小，则说明最小值存在于low和mid之间，且mid值有可能是最小值，因此high=mid
        # 如果mid指向值和high指向值一样大小，则无法判断最小值的位置，需要令high-=1进行遍历
        # 当low指针大于等于high指针时跳出循环，输出low指针指向值既是最小值。

        # 这道题有很多小坑，比如如果用mid处的值和数组左边的值比较，会有什么不同；else语句中如果不让right处的指向左移一位，而是让left处的指针右移一位会怎么样，都是需要稍加留意的地方。
        # write code here
        if not rotateArray or len(rotateArray) == 0:
            return 0
        low = 0
        high = len(rotateArray) - 1
        
        while low < high:
            mid = (low + high) // 2
            if rotateArray[mid] > rotateArray[high]:
                low = mid + 1
            elif rotateArray[mid] < rotateArray[high]:
                high = mid
            else:
                high -= 1
        return rotateArray[low]

if __name__ == '__main__':
    rotateArray = [3,4,5,1,2]
    print(Solution().minNumberInRotateArray(rotateArray))
    print(Solution().minNumberInRotateArray([1,1,1,0,1]))
    print(Solution().minNumberInRotateArray([1,0,1,1,1,1]))