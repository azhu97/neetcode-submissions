class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ss = set(["}", ")", "]"])
        for char in s:
            if char not in ss:
                stack.append(char)
            else:
                if not stack:
                    return False
                temp = stack.pop()
                
                if char == "}" and temp != "{":
                    return False
                if char == ")" and temp != "(":
                    return False
                if char == "]" and temp != "[":
                    return False
        
        return len(stack) == 0