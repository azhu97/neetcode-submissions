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
        res = []
        
        def bfs(u, v): # return if u is can reach v
            nonlocal mapping
            q = deque([u])
            curr = None
            while q:
                curr = q.popleft()
                if curr == v:
                    return True
                for c in mapping[curr]:
                    q.append(c)
            return False
        
        for u, v in queries:
            res.append(bfs(u,v))
        
        return res