# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        arr_ref = []
        stack = []
        
        current = head
        counter = 0
        ccc = current
        
        while ccc:
            arr_ref.append(ccc)
            ccc = ccc.next
            
        while current:
            
            if not stack:
                stack.append(counter)
            
            else:
                while stack and arr_ref[stack[-1]].val < current.val:
                    
                    arr_ref[stack.pop()] = None
                   
                    
                stack.append(counter)
                    
        
            current = current.next
            counter += 1
            
        dummy = ListNode()
        saved = dummy
        for x in arr_ref:
            if x:
                dummy.next = x
                x.next = None
                dummy = dummy.next

        return saved.next