class Solution:
    def hammingWeight(self, n: int) -> int:
        # unsigned integer n
        # return the number of 1 in the binary representation
        # most 32
        res = 0
        for i in range(32):
            if (1 << i) & n:
                res += 1
        return res