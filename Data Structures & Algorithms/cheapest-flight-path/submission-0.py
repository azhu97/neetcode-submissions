class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 1 directional array
        # there are no duplicates flights, no loops either
        adj_list = defaultdict(list)
        for a, b, cost in flights:
            adj_list[a].append((b, cost))
        
        def di(node):
            # when adding the heap
            # encapsulate
            # 1. cost
            # 2. remaining stops
            # 3. node
            heap = [(0, k, src)]
            visited = set() 
            while heap and len(visited) < n:
                cost, remain, airport = heapq.heappop(heap)
                print(cost, remain, airport)
                if airport == dst:
                    return cost
                if remain < 0:
                    # we can't jump anywhere from here
                    # we can't even visit this stop
                    continue
                remain -= 1
                visited.add(airport)
                for a, c in adj_list[airport]:
                    if a in visited:
                        continue
                    heapq.heappush(heap, (cost + c, remain, a))
            return -1 

        return di(src)
                