# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        answer = []
        
        while head:
            answer.append(head.val)
            head = head.next
            
        left = 0
        right = k - 1
        
        while right < len(answer):
            saced = right
            sa = left
            while left < right:
                answer[left], answer[right] = answer[right], answer[left]
                left += 1
                right -= 1
            left = sa + k
            right = saced + k
    
        dummy = ListNode(0)
        head = dummy
        
        for number in answer:
            dummy.next = ListNode(number)
            dummy = dummy.next
        
        return head.next