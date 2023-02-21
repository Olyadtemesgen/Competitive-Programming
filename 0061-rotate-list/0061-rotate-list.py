# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        current = head
        
        if not current:
            return None
        
        if not current.next:
            return head

        counter = 1
        while current.next:
            counter += 1
            current = current.next
        
        

        if not k % counter:
            return head
        
        current.next = head
        k = counter - k % counter
        
        curr = head.next
        prev = head

        while k - 1:
            prev = prev.next
            curr = curr.next
            k -= 1

        prev.next = None
        return curr