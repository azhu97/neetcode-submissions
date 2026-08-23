class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for u, v, time in times:
            adj_list[u].append((time, v))

        res = 0 
        visited = set()
        heap = [] 
        heapq.heappush(heap, (0, k))
        
        while heap and len(visited) < n:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            res = max(res, time)
            for t, ngbr in adj_list[node]:
                if ngbr in visited:
                    continue
                heapq.heappush(heap, (time + t, ngbr))
        return res if len(visited) == n else -1
        
