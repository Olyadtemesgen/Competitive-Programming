# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        previous, current, nexts = head, head.next, head.next.next
        
        while nexts:
            current.next = previous
            previous = current
            current = nexts
            nexts = nexts.next
            
        
        head.next = None
        current.next = previous
        
        return current