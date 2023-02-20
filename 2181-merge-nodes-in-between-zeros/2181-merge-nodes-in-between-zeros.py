# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Create a dummy node to act as the head of the new linked list
        dummy = ListNode(0)
        # Create a variable to keep track of the current node in the new linked list
        returned = dummy
        # Set the header to be the next node in the original linked list
        header = head.next
        
        # If the next node in the original linked list is None, skip over all nodes in the original list that have a value of 0
        if header == 0:
            while header and not header.val:
                header = header.next
        
        # Iterate through the original linked list
        while header:
            
            # Create a variable to hold the sum of all nodes with a value in the original linked list
            val = 0
            
            # Iterate through all nodes with a value in the original linked list and add their values to the 'val' variable
            while header and header.val:
                val += header.val
                header = header.next
            
            # If the sum is not zero, create a new node with the sum as its value and add it to the new linked list
            if val:
                dummy.next = ListNode(val)
                dummy = dummy.next
            
            # Move to the next node in the original linked list
            header = header.next
        
        # Return the head of the new linked list
        return returned.next

    