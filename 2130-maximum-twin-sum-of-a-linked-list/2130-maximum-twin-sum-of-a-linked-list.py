# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        array = []
        
        while head:
            array.append(head.val)
            head = head.next
        
        left = 0
        right = len(array) - 1
        
        maximum = 0
        
        while left < right:
            maximum = max(maximum, array[left] + array[right])
            
            right -= 1
            left += 1
        
        return maximum