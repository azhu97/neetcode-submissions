class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        def recurse(numLeft, numRight, n):
            if numLeft == numRight == n:
                res.append("".join(stack))
                return
            if numLeft < n:
                stack.append("(")
                recurse(numLeft + 1, numRight, n)
                stack.pop()
            if numRight < numLeft:
                stack.append(")")
                recurse(numLeft, numRight + 1, n)
                stack.pop()
        
        recurse(0, 0, n)
        return res
        
