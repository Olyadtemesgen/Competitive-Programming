# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        if not headA or not headB:
            return None
        
        prev = headA
        prev1 = headB
        
        while prev != prev1:
            
            if not prev:
                prev = headB
            
            else:
                prev = prev.next
            
            if not prev1:
                prev1 = headA
            
            
            
            
            else:
                prev1 = prev1.next
            
        return prev