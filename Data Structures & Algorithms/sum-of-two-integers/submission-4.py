class Solution:
    def getSum(self, a: int, b: int) -> int:
        print(bin(a), bin(b))
        res = 0
        carry = 0
        for i in range(32): 
            res |= (((carry) ^ (a >> i) ^ (b >> i)) & 1) << i
            carry = 1 if ((carry & (a >> i)) | (carry & (b >> i)) | ((a >> i) & (b >> i))) & 1 else 0
            print(bin((((carry) ^ (a >> i) ^ (b >> i)) & 1) << i), carry)

        print(bin(res), print(bin(res ^ 0xffffffff)))
        return res if a >= 0 or b >= 0 else res ^ 0xffffffff