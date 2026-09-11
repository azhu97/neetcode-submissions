class Solution:
    def isHappy(self, n: int) -> bool:
        # can we call dfs on each number from
        visited = set()
        def dfs(i):
            nonlocal visited
            if i == 1:
                return True
            if i in visited:
                return False
            visited.add(i)
            happy = 0

            while i:
                number = i % 10
                happy += (number * number)
                i = i // 10
            
            return dfs(happy)
        
        return dfs(n)