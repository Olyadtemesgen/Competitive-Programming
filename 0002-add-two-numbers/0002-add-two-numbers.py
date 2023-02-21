# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        current1 = l1
        current2 = l2
        
        saved = 0
        dummy = ListNode()
        heads = dummy
        
        while current1 and current2:
            
            summ = (current1.val + current2.val + saved) % 10
            saved = (current1.val + current2.val + saved) // 10
            
            dummy.next = ListNode(summ)
            dummy = dummy.next
            
            current1 = current1.next
            current2 = current2.next
            
        while current1:
            summ = (current1.val + saved) % 10
            saved = (current1.val + saved) // 10
            
            dummy.next = ListNode(summ)
            dummy = dummy.next
            
            current1 = current1.next
        
        while current2:
            summ = (current2.val + saved) % 10
            saved = (current2.val + saved) // 10
            
            dummy.next = ListNode(summ)
            dummy = dummy.next
            
            current2 = current2.next
        
        if saved:
            dummy.next = ListNode(saved)
            dummy = dummy.next
        
        return heads.next