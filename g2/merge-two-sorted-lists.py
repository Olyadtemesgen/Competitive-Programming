# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head1 = list1
        head2 = list2
        dummy = ListNode(0)
        dummy2 = dummy
        while head1 and head2:
            
            if head1.val <= head2.val:
                dummy.next = head1
                dummy = dummy.next
                head1 = head1.next
                
            else:
                dummy.next = head2
                head2 = head2.next
                dummy = dummy.next
        
        while head1:
            dummy.next = head1
            dummy = dummy.next
            head1 = head1.next
        
        while head2:
            dummy.next = head2
            head2 = head2.next
            dummy = dummy.next
        
        return dummy2.next