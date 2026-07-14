# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None and l2 == None:
            return 0
        curr1 = l1
        curr2 = l2
        currNew = ListNode()
        res = currNew
        carry = 0 

        while curr1 or curr2:
            print(1)
            t1 = 0
            t2 = 0
            if curr1 != None:
                t1 = curr1.val
                curr1 = curr1.next
            if curr2 != None:
                t2 = curr2.val
                curr2 = curr2.next
            temp = t1 + t2 + carry
            carry = temp // 10
            temp = temp % 10
            currNew.val = temp
            if curr1 == None and curr2 == None:
                break
            currNew.next = ListNode()
            currNew = currNew.next
        
        if carry != 0:
            currNew.next = ListNode(carry, None)
        
        return res 
            
            
