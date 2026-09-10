class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = defaultdict(list)
        for a, b in prerequisites:
            premap[a].append(b)
        
        visited = set()

        def dfs(course):
            nonlocal visited
            nonlocal premap

            if course in visited:
                return False
            if premap[course] == []:
                return True
            
            visited.add(course)
            for pre in premap[course]:
                if not dfs(pre):
                    return False
            
            visited.remove(course)
            premap[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True