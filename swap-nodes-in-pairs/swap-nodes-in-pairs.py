# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # slow = head
        # fast = head.next

        # while fast and fast.next:

        #     slow.val, fast.val = fast.val, slow.val
            
        #     slow = slow.next.next
        #     fast = fast.next.next
        
        # if fast:
        #     slow.val, fast.val = fast.val, slow.val

        # return head
        dummy = head
        def swapper(head):
            
            if  head and head.next:
                head.val, head.next.val = head.next.val, head.val
                swapper(head.next.next)
            

        
        swapper(head)
        
        return dummy