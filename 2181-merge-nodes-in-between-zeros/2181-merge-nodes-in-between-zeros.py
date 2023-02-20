# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        returned = dummy
        header = head.next
        
        if header == 0:
            while header and not header.val:
                header = header.next
        
        while header:
            val = 0
            while header and header.val:
                val += header.val
                header = header.next
            if val:
                dummy.next = ListNode(val)
                dummy = dummy.next
            header = header.next
        return returned.next