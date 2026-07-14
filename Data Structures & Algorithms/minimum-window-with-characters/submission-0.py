class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res_l, res_r = None, None
        l, r = 0, 0
        shortest = float('inf')
        char_map = {}
        for c in t:
            if c in char_map:
                char_map[c] += 1
            else:
                char_map[c] = 1
        
        while r < len(s):
            r_char = s[r]
            if r_char in char_map:
                char_map[r_char] -= 1
            # push the left pointer in as far as possible
            # also make sure that left pointer exceed right
            while max(char_map.values()) <= 0 and l <= r:
                l_char = s[l]
                if l_char in char_map:
                    char_map[l_char] += 1
                temp = r - l + 1
                if temp < shortest:
                    shortest = temp
                    res_l, res_r = l, r
                l += 1
            r += 1

        if shortest == float('inf'):
            return ""
        return s[res_l : (res_r + 1)]
    



                


        