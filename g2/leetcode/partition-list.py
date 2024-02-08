# Definition for singly-linked list.
class ListNode:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        array1 = []
        array2 = []
        varr = head
        
        while head:
            if head.val < x:
                array1.append(head.val)
                
            else:
                array2.append(head.val)
            head = head.next
        
        if not array1:
            return varr
        
        head = ListNode(array1[0])
        current = head
        
        for xy in array1[1:]:
            current.next = ListNode(xy)
            current = current.next
        
        for abb in array2:
            current.next = ListNode(abb)
            current = current.next
        
        return head
    
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        left_ = left = ListNode(0)
        right_ = right = ListNode(0)
        
        while head:
            if head.val < x:
                left.next = ListNode(head.val)
                left = left.next
            
            else:
                right.next = ListNode(head.val)
                right = right.next
            # consistency
            head = head.next
        
        right.next = None
        left.next = right_.next
        
        return left_.next