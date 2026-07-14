class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #two pointer solution 
        i = 0
        j = len(heights) - 1
        max_area = 0 
        while i < j:
            first = heights[i]
            last = heights[j]
            width = j - i

            temp = width * min(first, last)
            
            if temp > max_area:
                max_area = temp
            
            if first < last:
                i += 1
            else:
                j -= 1
        
        return max_area