class Solution:
    def hammingWeight(self, n: int) -> int:
        # unsigned integer n
        # return the number of 1 in the binary representation
        # most 32
        res = 0
        for i in range(32):
            # if (i << i) & n:
                # res += 1
            if 1 & n:
                res += 1
            n >>= 1
        return res