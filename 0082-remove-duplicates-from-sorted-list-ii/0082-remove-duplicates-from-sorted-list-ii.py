# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def deleteDuplicates1(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        # Create an empty list to store the values of the linked list.
        lists = []
        # Traverse the linked list and append each value to the list.
        while head:
            lists.append(head.val)
            head = head.next
            
        # Create a new dummy node to store the result.
        dummy = ListNode(0)
        # Create a pointer to the dummy node.
        d = dummy
        
        # Iterate through the list of values and add each unique value to the result linked list.
        for x in lists:
            if lists.count(x) == 1:
                dummy.next = ListNode(x)
                dummy = dummy.next
        
        # Return the result linked list.
        return d.next
    
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a new dummy node to store the result.
        dummy = ListNode(10)
        
        # Create a pointer to the dummy node.
        du = dummy
        # Create a pointer to the current node.
        right = head
        
        # Traverse the linked list.
        while right:
            # Check if the current node has a duplicate value.
            idx = False
            while right.next and right.val == right.next.val:
                right = right.next
                idx = True
            
            # If the current node has a duplicate value, move to the next node.
            if idx:
                right = right.next
            
            # If the current node has a unique value, add it to the result linked list.
            if right and right.next and right.val != right.next.val:
                dummy.next = ListNode(right.val)
                right = right.next
                dummy = dummy.next
            
            # If the current node is the last node, add it to the result linked list.
            elif not right or not right.next:
                if right:
                    dummy.next = ListNode(right.val)
                    right = right.next
                
        # Return the result linked list.
        return du.next
