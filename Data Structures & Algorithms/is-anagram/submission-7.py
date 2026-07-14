class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for char in s:
            try:
                #find index
                indexOfChar = t.index(char)
                #remove index
                t = t[:indexOfChar] + t[indexOfChar + 1:]
            except:
                return False
        return True
        