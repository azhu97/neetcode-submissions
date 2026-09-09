# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def helper(head):
            print("HELPER")
            nonlocal k
            # reverse the k, then return head and tail
            # check to see if there are even enough 
            curr = head
            for i in range(k):
                if curr == None:
                    return (head, None)
                curr = curr.next
            curr = head
            prev_node = None
            next_node = curr.next

            for i in range(k):
                # reverse the curr node
                curr.next = prev_node
                prev_node = curr
                curr = next_node 
                next_node = curr.next if curr else None
            print(f"returning ({prev_node}, {head})")
            return (prev_node, head)
        points = []
        curr = head
        temp = 0
        while curr:
            if temp % 3 == 0:
                points.append(curr)
            temp += 1
            curr = curr.next
        for i in range(len(points)):
            points[i] = helper(points[i])
        
        start, end = points[0]
        for i in range(1, len(points)):
            end.next = points[i][0]
            start, end = points[i]
        return points[0][0]
        
        
