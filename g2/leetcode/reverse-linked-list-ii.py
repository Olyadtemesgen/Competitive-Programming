# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        answer = []
        size = 0
        while head:
            size += 1
            answer.append(head.val)
            head = head.next
        
            
        dummy = ListNode(0)
        dd = dummy
        left -= 1
        right -= 1

        while left < right:
            answer[left], answer[right] = answer[right], answer[left]
            left += 1
            right -= 1   

        for x in answer:
            dummy.next = ListNode(x)
            dummy = dummy.next
        
        return dd.next