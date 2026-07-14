class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = Counter(s), Counter(t)
        keys = t.keys()
        for key in keys:
            print(key)
            if s.get(key, 0) != t.get(key, 0):
                return key
        return "lkasjdflkjasd"