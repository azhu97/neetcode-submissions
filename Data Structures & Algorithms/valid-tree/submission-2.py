from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n <= 1 and len(edges) == 0:
            return True
        # how can we detect a cycle?
        # if an edge connects two components that have already been "added" to the tree
        # so we want to see if 
        # 1. all nodes a reachable
        # 2. there is no cycle
        # the first thing, we have to build a mapping
        mapping = defaultdict(list)
        for u, v in edges:
            mapping[u].append(v)
            mapping[v].append(u)
        print(mapping)
        que = deque([edges[0][0]])
        visted_set = set()
        while que:
            curr = que.popleft()
            visted_set.add(curr)
            for node in mapping[curr]:
                if node in visted_set:
                    continue
                que.append(node)
        
        # we can automatically rule out its not a tree if not all nodes connect
        if len(visted_set) != n:
            return False
        
        # check for a cycle
        visited_set = set()
        for u, v in edges:
            if u in visited_set and v in visited_set:
                return False
            visited_set.add(u)
            visited_set.add(v)
        return True