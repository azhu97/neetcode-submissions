class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map = {}
        longest = 0
        l = 0
        r = 0

        while r < len(s):
            temp_char = s[r]
            if temp_char in char_map:
                char_map[temp_char] += 1
            else:
                char_map[temp_char] = 1
            most = max(char_map.values())
            
            if (r - l + 1) - most <= k:
                if (r - l + 1) > longest:
                    longest = r - l + 1
            else:
                while (r - l + 1) - most > k:
                    l_char = s[l]
                    char_map[l_char] -= 1
                    l += 1
                    most = max(char_map.values())
            r += 1

        return longest
        
                    

        