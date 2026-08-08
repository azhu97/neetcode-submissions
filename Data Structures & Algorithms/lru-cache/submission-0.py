class LRUCache:
    class Node:
        def __init__(self, key: int, val: int, next_node=None, prev_node=None):
            self.key = key
            self.val = val
            self.next_node = next_node
            self.prev_node = prev_node 

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.head = None  # Most Recently Used (MRU)
        self.tail = None  # Least Recently Used (LRU)
        self.mapping = {}

    def add(self, node: Node):
        """Adds node to the head of the doubly-linked list (MRU position)."""
        node.next_node = self.head
        node.prev_node = None
        
        if self.head is not None:
            self.head.prev_node = node
        self.head = node

        if self.tail is None:
            self.tail = node

    def remove(self, node: Node):
        """Removes an arbitrary node from the doubly-linked list."""
        if node.prev_node is not None:
            node.prev_node.next_node = node.next_node
        else:
            self.head = node.next_node

        if node.next_node is not None:
            node.next_node.prev_node = node.prev_node
        else:
            self.tail = node.prev_node

        node.next_node = None
        node.prev_node = None

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1 
        
        node = self.mapping[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            # Update existing node value and move to MRU position
            node = self.mapping[key]
            node.val = value
            self.remove(node)
            self.add(node)
            return

        if self.count >= self.capacity:
            # Evict LRU node from both mapping and list
            del self.mapping[self.tail.key]
            self.remove(self.tail)
            self.count -= 1

        # Insert new node
        new_node = self.Node(key, value)
        self.add(new_node)
        self.mapping[key] = new_node
        self.count += 1