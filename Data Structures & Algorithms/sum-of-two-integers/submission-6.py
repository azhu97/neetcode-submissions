class Solution:
    def getSum(self, a: int, b: int) -> int:
        return a + b
        print(bin(a), bin(b))
        res = 0
        carry = 0
        for i in range(32): 
            res |= (((carry) ^ (a >> i) ^ (b >> i)) & 1) << i
            carry = 1 if ((carry & (a >> i)) | (carry & (b >> i)) | ((a >> i) & (b >> i))) & 1 else 0
 
        print(bin(res), bin(res ^ 0xffffffff))
        print(bin(-7))
        return res if a >= 0 or b >= 0 else res ^ 0xffffffff