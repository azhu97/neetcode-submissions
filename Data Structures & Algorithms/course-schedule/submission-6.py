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
        print(s)
        
        ### can't we just run bfs on each node? runtime would be same 
        def bfs(start):
            nonlocal adj_list
            que = deque([start])
            visited_set = set()
            while que:
                node = que.popleft()
                visited_set.add(node)
                for n in adj_list[node]:
                    print(node, n)
                    if n in visited_set:
                        return False
                    que.append(n)
            return True
        print("Here")
        for i in s:
            print("Here")
            if not bfs(i):
                return False
        
        if len(s) == 0:
            return False
        return True
            