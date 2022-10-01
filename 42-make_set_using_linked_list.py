class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#i mis undestand the concept and did this. Poor me
class Solution:
    def deleteDuplicates(self, head):
        current = slow = fast = ListNode(0, next=head)
        while fast.next:
            if slow.val == fast.val:
                fast = fast.next
            slow.next = fast
            slow = slow.next
            fast = fast.next
        return current.next
