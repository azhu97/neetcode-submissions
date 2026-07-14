class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []
        
        for i, num in enumerate(nums):
            heapq.heappush(heap, (-num, i))

            if i >= k - 1:
                while heap:
                    value, index = heap[0]
                    value *= -1
                    if index >= (i - k + 1):
                        res.append(value)
                        break
                    heapq.heappop(heap)

        return res