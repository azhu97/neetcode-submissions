# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        dummy = ListNode(0, 0)
        curr = dummy
        while list1 and list2: # when both are not none
            if list1.val <= list2.val:
                curr.next = ListNode(list1.val)
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                curr = curr.next
                list2 = list2.next
        
        while list1:
            curr.next = ListNode(list1.val)
            curr = curr.next
            list1 = list1.next
        while list2:
            curr.next = ListNode(list2.val)
            curr = curr.next
            list2 = list2.next
    
        return dummy.next