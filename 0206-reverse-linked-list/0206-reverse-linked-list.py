# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head
        
        array = []
        
        while current:
            array.append(current.val)
            current = current.next
        if not array:
            return None
        array.reverse()
        self.head = ListNode(array[0])
        length = 0
        current = self.head
        
        while length < len(array) - 1:
            current.next = ListNode(array[length + 1])
            current = current.next
            length += 1
        
        return self.head