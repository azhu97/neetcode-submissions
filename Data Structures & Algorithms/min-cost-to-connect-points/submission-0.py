class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # points[i] = [xi, yi]
        # cost of connecting 2 points -> |xi - xj| + |yi - yj|

        # run prims algorithm
        # this would be O((time to make adj_list) * prims) -> around O(n^2)
        # no cycles
        def distance(point1, point2):
            x1, y1 = point1
            x2, y2 = point2
            return abs(x1 - x2) + abs(y1 - y2)
        
        n = len(points) # number of points 
        # we should label each point by their index in points, zero indexed
        adj_list = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                adj_list[i].append((distance(points[i], points[j]), j))
        
        # now run prims, starting on 0
        res = 0
        heap = []
        heapq.heappush(heap, (0, 0))
        visited = set()
        while heap and len(visited) < n:
            cost, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            res += cost
            for c, ngbr in adj_list[node]:
                # cost and node
                if ngbr in visited:
                    continue
                heapq.heappush(heap, (c, ngbr))
        
        return res

                