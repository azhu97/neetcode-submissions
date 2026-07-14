# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None
        print(not head or not head.next)
        arr = []
        curr = head
        while curr != None:
            arr.append(curr)
            curr = curr.next
        
        dummy = ListNode(0, None)
        curr = dummy
        l, r = 0, len(arr) - 1
        while l <= r:
            curr.next = arr[l]
            curr = curr.next
            if l != r:
                curr.next = arr[r]
                curr = curr.next
                r -= 1
            l += 1
        curr.next = None