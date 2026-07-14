# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        head = None
        temp = None
        curr1 = list1
        curr2 = list2
        
        if curr1.val < curr2.val:
            temp = curr1
            head = temp
            curr1 = curr1.next
        else:
            temp = curr2
            head = temp
            curr2 = curr2.next

        while curr1 != None and curr2 != None:
            if curr1.val < curr2.val:
                temp.next = curr1
                temp = temp.next
                curr1 = curr1.next
            else:
                temp.next = curr2
                temp = temp.next
                curr2 = curr2.next
        
        while curr1 != None:
            temp.next = curr1
            temp = temp.next
            curr1 = curr1.next
        while curr2 != None:
            temp.next = curr2
            temp = temp.next
            curr2 = curr2.next

        return head
