# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        current = other = this = ListNode(0, head)
        while n:
            this = this.next
            n -= 1
        fast = this
        while fast.next:
            fast = fast.next
            other = other.next
        other.next = other.next.next
        return current.next
