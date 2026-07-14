class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        curr_counter = defaultdict(int)
        l, r = 0, 0
        #expand when l_char is not part of counter or curr_counter[l_char] exceeds
        while r < len(s2):
            r_char = s2[r]
            curr_counter[r_char] += 1

            while l <= r and (s2[r] not in counter or curr_counter[s2[r]] > counter[s2[r]]):
                curr_counter[s2[l]] -= 1
                if curr_counter[s2[l]] == 0:
                    del(curr_counter[s2[l]])
                l += 1

            if (r - l + 1) == len(s1) and curr_counter == counter:
                return True

            r += 1
        
        return False


        