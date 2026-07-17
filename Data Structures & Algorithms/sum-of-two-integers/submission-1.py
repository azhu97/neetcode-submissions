class Solution:
    def getSum(self, a: int, b: int) -> int:
        print(bin(a), bin(b))
        res = 0
        carry = 0
        for i in range(32): 
            res |= (((carry) ^ (a >> i) ^ (b >> i)) & 1) << i
            carry = ((a >> i) & (b >> i)) & 1 
            print((((carry) ^ (a >> i) ^ (b >> i)) & 1) << i, carry)
        #    print(((((carry) ^ (a >> i) ^ (b >> i)) & 1) << i), carry)

        print(bin(10), bin(res))
        return res if a >= 0 and b >= 0 else res ^ 0xffffffff