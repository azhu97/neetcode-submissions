class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # num of courses = total number of courses, labled from 0 to numCourses - 1
        # prereq[i] = [ai, bi], must take ai before you take bi
        # [0, 1], must take course0 before course1
        # prereqs can be indirect
        # queries, queries[j] = [uj, vj], for the jth query, you should answer whether course uj is a prereq to vj
        # hard bethod, run bfs to see if uj, is reachble
        #run ime would be (e + l) * queries -> 15 * 10,000 
        mapping = defaultdict(set)
        for i, j in prerequisites:
            mapping[i].add(j)
        adj_list = defaultdict(set) # u = [], u can reach whatever is in the set
        
        def bfs(u): # return if u is can reach v
            nonlocal adj_list
            visted = set()
            q = deque([u])
            curr = None
            while q:
                curr = q.popleft()
                visted.add(curr)
                adj_list[u].add(curr)
                for c in mapping[curr]:
                    if c in visted:
                        continue
                    q.append(c)
            
        for i in range(numCourses):
            bfs(i)
        
        res = []
        for u, v in queries:
            if v in adj_list[u]:
                res.append(True)
            else:
                res.append(False)
        return res