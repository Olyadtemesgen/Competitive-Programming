# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lists = []
        while head:
            lists.append(head.val)
            head = head.next
            
        dummy = ListNode(0)
        d = dummy
        
        for x in lists:
            if lists.count(x) == 1:
                dummy.next = ListNode(x)
                dummy = dummy.next
        
        return d.next
        dummy = ListNode(-1)
        du = dummy
        right = head
        
        while right:
            
            idx = False
            
            while right.next and right.val == right.next.val:
                right = right.next
                idx = True
            
            if idx:
                right = right.next
            
            if right.next and right.val != right.next.val:
                dummy.next = right
                right = right.next
                dummy = dummy.next
            
            elif not right.next:
                right = right.next
        return du.next