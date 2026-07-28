from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adj list and starting node set
        adj_list = defaultdict(list)
        s = set()
        v_s = set()
        for u, v in prerequisites:
            s.add(u)
            v_s.add(v)
            if v in s:
                print("Early False")
                return False
            adj_list[u].append(v)
        
        s = set()
        for i in range(numCourses):
            if i not in v_s:
                s.add(i)
        

        
        # now run bfs
        que = deque(list(s))
        s = set()
        while que:
            node = que.popleft()
            print(node)
            s.add(node)
            for adj in adj_list[node]:
                if adj not in s:
                    que.append(adj)
        
        return len(s) == numCourses

        
        