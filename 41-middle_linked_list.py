class Solution:
    def middleNode(self, head):
        counter = 0
        x = head
        while head:
            counter += 1
            head = head.next
        value = counter // 2
        while value:
            x = x.next
            value -= 1
        return x
