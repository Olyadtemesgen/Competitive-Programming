# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        #first let us find the mid and reverse the half mid
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        current = slow
        previous = None
        
        #this code reverse the above half of the linked list
        while current:
            current.next, previous, current = previous, current, current.next
        
        maximum = 0
        
        while previous:
            
            maximum = max(maximum, previous.val + head.val)
            head = head.next
            previous = previous.next
        
        return maximum
    #this works but with space complexity of O(N)
    def pairSum1(self, head: Optional[ListNode]) -> int:

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