class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(stack, leftCount ,rightCount):
            if leftCount == rightCount == n:
                res.append("".join(stack))
                return
            
            if leftCount < n:
                stack.append("(")
                backtrack(stack, leftCount + 1, rightCount)
                stack.pop()
            if rightCount < leftCount:
                stack.append(")")
                backtrack(stack, leftCount, rightCount + 1)
                stack.pop()

        backtrack([], 0, 0)
        return res
            