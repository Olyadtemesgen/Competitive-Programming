# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        # slow = head
        # fast = head.next

        # while fast and fast.next:

        #     slow.val, fast.val = fast.val, slow.val
            
        #     slow = slow.next.next
        #     fast = fast.next.next
        
        # if fast:
        #     slow.val, fast.val = fast.val, slow.val

        # return head

        dummy = ListNode(0, head)

        prev, current = dummy, head
        while current and current.next:

            next_pair = current.next.next
            second = current.next

            second.next = current
            current.next = next_pair
            prev.next = second

            prev = current
            current = next_pair
        # if current:

        return dummy.next