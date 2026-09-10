class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # do it like course schedule II
        # run dfs on each numCourse, keeping a visited set to check for cycles
        # once we clear, we clear the prereq of the course
        # use visited for current dfs path only
        res = []
        res_set = set() # keep track so we can skip on dfs start
        visited = set()
        mapping = defaultdict(list)
        for a,b in prerequisites:
            mapping[a].append(b)
        
        # add course to mapping 
        def dfs(course):
            nonlocal res, res_set, visited, mapping
            if course not in res_set:
                res_set.add(course)
                res.append(course)

            if course in visited:
                return False
            if mapping[course] == []:
                # means that we have reached a course that doesn't require a pre
                # or has guranteed its course
                return True

            visited.add(course)
            for pre in mapping[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            
            # all pre reqs are cleared
            mapping[course] = []
            return True 
        
        for course in range(numCourses):
            if course in res_set:
                continue
            result = dfs(course)
            if not result:
                return []
        return res