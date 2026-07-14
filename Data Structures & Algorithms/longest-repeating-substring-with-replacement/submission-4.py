class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map = defaultdict(int)
        l, r = 0, 0
        longest = 0

        while r < len(s):
            r_char = s[r]
            char_map[r_char] += 1
            most = max(char_map.values())
            while (r - l + 1) - most > k:
                l_char = s[l]
                char_map[l_char] -= 1
                most = max(char_map.values())
                l += 1
            longest = max(longest, r - l + 1)
            r += 1

        return longest

