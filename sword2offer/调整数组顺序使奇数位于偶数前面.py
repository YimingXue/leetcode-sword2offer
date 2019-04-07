# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # 使用冒泡法进行求解，从后往前使用i,j指针进行判定
        # j指针指向下一个要放入偶数的位置，i指针用来遍历数组
        # 需要注意的是第一个判定的数字一定要是奇数，否者会陷入循环
        # 还有数组只有一个元素和没有元素时的情况需要进行判定
        # write code here
        if len(array) <= 1:
            return array
        i = len(array)-1
        j = len(array)-1
        while array[i] & 1 == False:
            i -= 1
            j -= 1
        while i >= 0:
            if array[i] & 1 == True:
                i -= 1
            else:
                for k in range(i, j):
                    array[k], array[k+1] = array[k+1], array[k]
                j -= 1
        return array


if __name__ == '__main__':
    array = [1,2,3,4,5,6]
    print(Solution().reOrderArray(array))
