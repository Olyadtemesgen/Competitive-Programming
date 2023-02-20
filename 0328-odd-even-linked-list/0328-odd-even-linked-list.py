# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        odd = ListNode(0)
        even = ListNode(0)
        
        startodd = odd
        starteven = even
        count = 1
        
        while head:
            
            if count % 2:
                odd.next = head
                head = head.next
                odd = odd.next
                odd.next = None
            
            else:
                even.next = head
                head = head.next
                even = even.next
                even.next = None
                
            count += 1
        odd.next = starteven.next
        
        return startodd.next