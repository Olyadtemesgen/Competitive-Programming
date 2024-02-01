# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        array = []

        while cur:
            array.append(cur.val)
            cur = cur.next
            
        array.sort()

        dummy = ListNode(0)
        other = dummy
        for x in array:
            dummy.next = ListNode(x)
            dummy = dummy.next
        
        return other.next

        current = head
        
        while current:
            
            real_pointer = head
            
            while real_pointer != current:
                
                if real_pointer.val > current.val: 
                    real_pointer.val, current.val = current.val, real_pointer.val
                
                real_pointer = real_pointer.next
            
            current = current.next
        
        return head
