class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []
        for char in s:
            if char.isalpha() or char.isnumeric():
                temp.append(char)
        s = "".join(temp)
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
