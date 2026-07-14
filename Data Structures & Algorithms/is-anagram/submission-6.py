class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for char in s:
            try:
                #find index
                indexOfChar = t.index(char)
                #remove index
                t = t[:indexOfChar] + t[indexOfChar + 1:]
            except:
                return False
        if len(t) != 0:
            return False
        return True
        