# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.length = 0

        current = self.head
        while current:
            self.length += 1
            current = current.next

    def getRandom(self) -> int:

        randosm = random.randint(1,self.length)
        
        current = self.head

        while randosm - 1:
            current = current.next
            randosm -= 1
        
        if current:
            return current.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()