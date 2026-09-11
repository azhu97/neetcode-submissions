class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 1 directional array
        # there are no duplicates flights, no loops either
        adj_list = defaultdict(list)
        for a, b, cost in flights:
            adj_list[a].append((b, cost))
        
        def di():
            heap = [(0, k + 1, src)]      # edges remaining, not stops
            best = {}                      # node -> max edges remaining when popped
            while heap:
                cost, remain, airport = heapq.heappop(heap)
                if airport == dst:
                    return cost
                if remain == 0:
                    continue
                if best.get(airport, -1) >= remain:
                    continue
                best[airport] = remain
                for a, c in adj_list[airport]:
                    heapq.heappush(heap, (cost + c, remain - 1, a))
            return -1

        return di()
                