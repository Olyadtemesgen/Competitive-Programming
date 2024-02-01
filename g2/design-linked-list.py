class Node:
    def __init__(self, val, nex):
        self.next = nex
        self.val = val
        
class MyLinkedList:

    def __init__(self):
        
        self.head  = None
        self.size = 0

        
    def get(self, index: int) -> int:
        
        if not self.head:
            return -1
        
        dummy = self.head
        i = 0
        while i < index and dummy != None:
            dummy = dummy.next
            i += 1
        
        if dummy:
            return dummy.val
        
        return -1
        

    def addAtHead(self, val: int) -> None:
        
        node = Node(val, self.head)
        self.head = node
            
    def addAtTail(self, val: int) -> None:
        
        if not self.head:
            self.head = Node(val, None)
            return
        
        dummy = self.head
        
        if not dummy:
            self.head = Node(val, None)
        
        while dummy.next:
            dummy = dummy.next
        
        dummy.next = Node(val, None)
        self.size += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        
        if index == 0:
            self.addAtHead(val)
            return
        
        inserted = Node(val, None)
        
        bef = None
        curr = self.head
        i = 0
        
        while curr and i < index:
            i += 1
            bef = curr
            curr = curr.next
        
        if index == i:
            
            inserted.next = curr
            bef.next = inserted
        
    def deleteAtIndex(self, index: int) -> None:
        
        dummy = self.head
        
        if index == 0:
            if self.head:
                self.head = self.head.next
            
            return
        
        i = 0
        while i < index - 1 and dummy:
            dummy = dummy.next
            i += 1
        
        if i == index - 1:
            
            if dummy:
                
                if dummy.next:
                    dummy.next = dummy.next.next
        
                
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)