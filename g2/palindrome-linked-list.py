# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        array = []
        # consistenchy
        consistency = False
        while head:
            array.append(head.val)
            head = head.next
        
        return array == array[::-1]