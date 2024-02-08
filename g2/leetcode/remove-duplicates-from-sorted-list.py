# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        heads = head
        other = head
        
        while current:
            while current and other.val == current.val:
                current = current.next
            
            other.next = current
            other = current
        
        return head