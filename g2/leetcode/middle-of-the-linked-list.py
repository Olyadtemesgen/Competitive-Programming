class Solution:
    def middleNode2(self, head):
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


    def middleNode1(self, head):
        
        result = []
        current = head
        
        while current:
            result.append(current)
            current = current.next
        
        return result[len(result)//2]
    
    def middleNode(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow