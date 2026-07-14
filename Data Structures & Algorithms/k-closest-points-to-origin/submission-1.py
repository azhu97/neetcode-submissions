class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            temp = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, (temp, ([x, y])))
            
        res = []
        for i in range(k):
            temp = heapq.heappop(heap)
            res.append(temp[1])

        return res
        