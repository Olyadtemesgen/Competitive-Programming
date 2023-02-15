# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        answer = []
        for linked_list in lists:
            while linked_list:
                answer.append(linked_list.val)
                linked_list = linked_list.next
        
        answer.sort()

        dummy = ListNode(0)
        head = dummy

        for x in answer:
            dummy.next = ListNode(x)
            dummy = dummy.next
        
        return head.next