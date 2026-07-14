class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        nums = Counter(nums)

        for key, value in nums.items():
            heapq.heappush(heap, (-value, key))
        
        res = []
        for i in range(k):
            key, value = heapq.heappop(heap)
            res.append(value)
        
        return res