# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Create two dummy nodes, odd and even, and store them in startodd and starteven, respectively
        odd = ListNode(0)
        even = ListNode(0)
        startodd = odd
        starteven = even
        
        # Initialize count to 1 and iterate over the input linked list
        count = 1
        while head:
            
            # If count is odd, append the current node to the odd list
            if count % 2:
                odd.next = head
                head = head.next
                odd = odd.next
                odd.next = None
            
            # If count is even, append the current node to the even list
            else:
                even.next = head
                head = head.next
                even = even.next
                even.next = None
                
            # Increment count by 1
            count += 1
        
        # Concatenate the odd and even lists and return the modified linked list
        odd.next = starteven.next
        return startodd.next
