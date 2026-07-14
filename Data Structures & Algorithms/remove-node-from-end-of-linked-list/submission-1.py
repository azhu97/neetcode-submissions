# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp_array = []
        current = head
        while current != None:
            temp_array.append(current)
            current = current.next
        
        count = len(temp_array)
        count -= n
        if count == 0:
            head = head.next
        else:
            current = temp_array[count - 1]
            if current.next != None:
                current.next = current.next.next
            
        return head