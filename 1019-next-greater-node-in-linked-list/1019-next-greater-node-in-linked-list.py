# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        stack = []
        
        current = head
        array = []
        counter = 0
        while current:
            
            if not stack:
                
                stack.append(counter)
                
            else:
                
                while stack and array[stack[-1]] < current.val:
                    array[stack.pop()] = current.val
                    
                stack.append(counter)
            
            counter += 1
            array.append(current.val)
            current = current.next
        
        array[-1] = 0

        while stack:
            array[stack.pop()] = 0
            
        return array