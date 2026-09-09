class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # queries -> points
        # query[j] is the length of the shoretst interval i such that left <= query[j] <= right
        # return -1 if no interval exists
        # brute force (o(n^2))
        res = [-1 for i in range(len(queries))]
        intervals.sort()
        sorted_q = sorted((queries[i], i) for i in range(len(queries)))
        heap = []
        l, r = 0, 0 # l for intervals, r for queries
        while r < len(queries):
            q, index = sorted_q[r]
            while l < len(intervals) and intervals[l][0] <= q:
                heapq.heappush(heap, (intervals[l][1] - intervals[l][0] + 1, intervals[l][0], intervals[l][1]))
                l += 1
            while heap:
                # check if bounds work 
                if heap[0][1] <= q <= heap[0][2]:
                    res[index] = heap[0][0]
                    break
                else:
                    heapq.heappop(heap)
            r += 1
        
        return res