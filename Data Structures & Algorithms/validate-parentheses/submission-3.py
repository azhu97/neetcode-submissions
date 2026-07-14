class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"}":"{", "]":"[", ")":"("}
        stack = []

        for char in s:
            if char in pairs.values():
                stack.append(char)
            else:
                if len(stack) == 0 or stack.pop() != pairs[char]: 
                    return False
        if len(stack) > 0:
            return False
        return True