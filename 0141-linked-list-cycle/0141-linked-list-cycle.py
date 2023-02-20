# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        sets = set()

        current = head
        while current:
            if current in sets:
                return True
            sets.add(current)
            current = current.next
        
        return False
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        if head:
            fast = head.next
        else:
            return None
            
        while fast and fast.next:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        
        return False