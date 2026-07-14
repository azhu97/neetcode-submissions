class MinStack:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        
        if self.head == None:
            self.head = MinStack.Node(val, None, val)
        else:
            temp_node = MinStack.Node(val, self.head, min(self.head.mini, val))
            self.head = temp_node
            
    def pop(self) -> None:
        current = self.head.next_node
        self.head.next_node = None
        self.head = current

    def top(self) -> int:
        if self.head == None:
            return
        return self.head.data 

    def getMin(self) -> int:
        if self.head == None:
            return
        return self.head.mini
    
    class Node:
        def __init__(self, data, next_node, mini):
            self.data = data
            self.next_node = next_node
            self.mini = mini
        
