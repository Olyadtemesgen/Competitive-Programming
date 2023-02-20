# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # This method finds the maximum sum of pairs from the linked list.
    # It reverses the second half of the linked list for easier traversal and
    # comparison with the first half.
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # Find the middle of the linked list.
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse the second half of the linked list.
        current = slow
        previous = None
        
        while current:
            current.next, previous, current = previous, current, current.next
        
        maximum = 0
        
        # Traverse both halves of the linked list and find the maximum sum of pairs.
        while previous:
            maximum = max(maximum, previous.val + head.val)
            head = head.next
            previous = previous.next
        
        return maximum

    # This method also finds the maximum sum of pairs from the linked list
    # but it uses an array to store the elements of the linked list.
    # It has a space complexity of O(N).
    def pairSum1(self, head: Optional[ListNode]) -> int:

        array = []
        
        # Add the elements of the linked list to an array.
        while head:
            array.append(head.val)
            head = head.next
        
        left = 0
        right = len(array) - 1
        
        maximum = 0
        
        # Traverse the array from both ends and find the maximum sum of pairs.
        while left < right:
            maximum = max(maximum, array[left] + array[right])
            right -= 1
            left += 1
        
        return maximum
