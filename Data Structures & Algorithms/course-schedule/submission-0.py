class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # numCourses, int
        # -> required to take, from 0 to numCourses - 1
        # prereq[i] = [a, b], must take b first if you want to take a
        # return if its possible to finish all coures 
        
        # don't even think about that, think about the secenarios where we can take courses
        # might be too many edge cases, just think about the other way 
        # lets take all the classes that don't require a prereq 
        # meaning that number doesn't appear in prereq[i][0] for all i
        prereq = defaultdict(set)
        need_pre = set()
        for i, j in prerequisites:
            # i is class, j i pre | j -> i
            need_pre.add(i)
            prereq[j].add(i)
        start = []
        for i in range(numCourses):
            if i not in need_pre:
                start.append(i)
        
        que = deque(start)
        visted = set()
        while que:
            take = que.popleft()
            visted.add(take)
            for next_class in prereq[take]:
                if next_class in visted:
                    continue
                que.append(next_class)
        return len(visted) == numCourses