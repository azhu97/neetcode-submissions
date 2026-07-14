class MinStack:
    class Node:
        def __init__(self, value, minimum):
            self.value = value
            self.minimum = minimum

    def __init__(self):
        self.stack = []        

    def push(self, val: int) -> None:
        prev_min = self.stack[-1].minimum if self.stack else float('inf')
        temp = self.Node(val, min(val, prev_min))
        self.stack.append(temp)

    def pop(self) -> None:
        self.stack.pop()


    def top(self) -> int:
        return self.stack[-1].value 

    def getMin(self) -> int:
        return self.stack[-1].minimum
        
