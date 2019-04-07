# -*- coding:utf-8 -*-
class Solution: 
    def Power(self, base, exponent):
        # write code here
        # return base ** exponent
        
        # 当n为偶数, a^n = a^(n/2) * a^(n/2) 
        # 当n为奇数, a^n = a^((n-1)/2) * a^((n-1)/2)) * a 
        # 利用右移一位运算代替除以2 
        # 利用位与运算代替了求余运算法%来判断一个数是奇数还是偶数
        if base-0.0 <= 0.0000001 and base-0.0 >= -0.0000001 and exponent != 0:
            return 0
        is_neg_base = base < 0; is_neg_exponent = exponent < 0
        base = abs(base); exponent = abs(exponent)
        res = self.getPower(base, exponent)
        res = -res if is_neg_base else res
        res = 1.0/res if is_neg_exponent else res
        return res
        
    def getPower(self, base, exponent):
        if exponent == 0:
            return 1
        elif exponent == 1:
            return base
        else:
            result = self.getPower(base, exponent>>1)
            result *= result
            if exponent & 1:
                result *= base
        return result

if __name__ == '__main__':
    base = 2
    exponent = 3
    print(Solution().Power(base, exponent))
    print(1.0/8)