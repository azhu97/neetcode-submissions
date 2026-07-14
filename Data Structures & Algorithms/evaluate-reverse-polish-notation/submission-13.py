class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op_set = (["*", "-", "+", "/"])
        for char in tokens:
            print(stack, char)
            if char not in op_set:
                stack.append(int(char))
            else:
                second = stack.pop()
                first = stack.pop()
                if char == "+":
                    temp = first + second
                elif char == "-":
                    temp = first - second
                elif char == "*":
                    temp = first * second
                else:

                    temp = abs(first) // abs(second)
                    if first * second < 0:
                        temp *= -1
                stack.append(temp)
        
        print(stack)
        return stack[0]
             