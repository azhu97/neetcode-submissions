from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # return true only if 
        # 1. all nodes are reachable 
        # don't think even need to check
        # 2. no cycle is formed from the edges -> cycle == livelock
        adj_list = defaultdict(list)
        class_require_prereq = set()
        for u, v in prerequisites:
            if u == v:
                return False
            adj_list[v].append(u)
            class_require_prereq.add(u)
        s = set() # valid starting nodes
        for i in range(numCourses):
            if i not in class_require_prereq:
                s.add(i)
        
        def dfs(i, visited_set):
            nonlocal adj_list
            if i in visited_set:
                return False
            visited_set.add(i)
            for ngbr in adj_list[i]:
                if dfs(ngbr, visited_set) == False:
                    return False
                visited_set.remove(ngbr)
            return True
                
                

        for i in s:
            if not dfs(i, set()):
                return False
        
        if len(s) == 0:
            return False
        return True
            