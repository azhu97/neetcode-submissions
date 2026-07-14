class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # this problem utilizes stack for most recent previous elements 
        res = [0] * len(temperatures)
        stack = [] # store tuples (temp, index)

        for i, temp in enumerate(temperatures):
            while len(stack) != 0 and stack[-1][0] < temp:
                tempT, tempI = stack.pop()
                res[tempI] = i - tempI
            stack.append((temp, i))
        
        return res
