class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # sliding window approach
        # push the right pointer when we can fit the fruit into one of the two baskets
        # push the left pointer 
        l_f, l_count = None, 0
        r_f, r_count = None, 0 
        res = 0
        l, r = 0, 0
        while r < len(fruits):
            fruit = fruits[r]
            if (l_f is None or r_f is None) and (fruit != l_f or fruit != r_f):
                # trivial case where one of the baskets is empty
                if l_f is None: l_f, l_count = fruit, 1
                else: r_f, r_count= fruit, 1
                print(1)
            else: # non trivial case, where both baskets have fruit
                # first two cases are triv
                if fruit == l_f:
                    print(2)
                    l_count += 1
                elif fruit == r_f:
                    print(3)
                    r_count += 1
                else:
                    print(4)
                    # we have a mismatch in fruit
                    while l_count > 0 and r_count > 0:
                        if fruits[l] == l_f:
                            l_count -= 1
                        else:
                            r_count -= 1
                        l += 1
                    if l_count == 0:
                        l_f, l_count = fruit, 1
                    else:
                        r_f, r_count = fruit, 1
            res = max(res, r - l + 1)
            r += 1
            print(l_f, r_f)
        
        return res