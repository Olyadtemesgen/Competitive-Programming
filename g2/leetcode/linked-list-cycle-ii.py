# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = fast = head
        
        while fast and fast.next:
            
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = head
                
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                
                return slow

        return None
    def detectCycle1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sets = set()
        # current
        current = head
        while current:
            if current in sets:
                return current
            sets.add(current)
            current = current.next
        
        return None