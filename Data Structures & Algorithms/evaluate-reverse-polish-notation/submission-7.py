class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            match char:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a - b)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(int(a / b))  # Truncate toward zero
                case _:
                    stack.append(int(char))
        return stack[0]

