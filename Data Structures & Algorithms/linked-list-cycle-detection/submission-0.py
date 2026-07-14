# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        set_of_nodes = set()
        cur = head

        while cur != None:
            print(cur)
            if cur in set_of_nodes:
                return True
            else:
                set_of_nodes.add(cur)
            cur = cur.next
        
        return False