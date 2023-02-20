# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        # initialize counter to keep track of current node index
        counter = 1
        
        # if linked list has less than 3 nodes, return [-1, -1]
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        # initialize pointers to current, previous, and next nodes
        current = head.next
        prev = head
        after = head.next.next
        
        # initialize variables to store the index of the first and last critical points,
        # the minimum distance between two critical points, and the number of critical points found
        first = 0
        last = 0
        minimum = float("inf")
        finder = 0
        
        while after:
            
            # if the current node is a critical point, update variables accordingly
            if current.val > prev.val and current.val > after.val:
                finder += 1
                
                if not first:
                    saved = counter
                    first = counter
                else:
                    minimum = min(minimum, counter - saved)
                    last = counter - first
                    saved = counter
            
            elif current.val < prev.val and current.val < after.val:
                finder += 1
                
                if not first:
                    first = counter
                    saved = counter
                else:
                    minimum = min(minimum, counter - saved)
                    last = counter - first
                    saved = counter
            
            counter += 1
            
            # move the pointers to the next set of three nodes
            prev = prev.next
            current = current.next
            after = after.next
        
        # if only one critical point is found, return [-1, -1]
        if finder <= 1:
            return [-1, -1]
        else:
            return [minimum, last]
