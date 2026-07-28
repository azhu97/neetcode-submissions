class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temp[i] represents teh daily temperature on the ith day
        # return an array, result, where result[i] is the number of days after the ith day,
        # days before a warmer temp appears on a future day
        res = [0 for i in range(len(temperatures))]
        stack = [] # (i, temp), pop until you can't
        for i, temp in enumerate(temperatures):
            print(f"At i = {i}")
            while stack and stack[-1][1] < temp:
                j, prev_temp = stack.pop()
                print(f"At j = {j}")
                res[j] = i - j
            stack.append((i, temp))
        
        return res