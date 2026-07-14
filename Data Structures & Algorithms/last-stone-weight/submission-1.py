class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-n for n in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x = -(heapq.heappop(heap))
            y = -(heapq.heappop(heap))
            temp = max(x, y) - min(x, y)
            if temp != 0:
                heapq.heappush(heap, -temp)

        if len(heap) == 0:
            return 0
        return -(heap[0])
        