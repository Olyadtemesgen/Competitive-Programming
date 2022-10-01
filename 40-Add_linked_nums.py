# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from xml.dom.minicompat import NodeList


class Solution:
    def addTwoNumbers(self, l1, l2):
        st1 = ""
        for x in range(max(len(l1), len(l2))):
            if x < min(len(l1), len(l2)):
                num = l1[x] + l2[x]
                if num >= 10:
                    st1 += str(num % 10)
                    if len(l1) > len(l2):
                        l1[x + 1] += 1
                    else:
                        l2[x + 1] += 1
                else:
                    st1 += str(num)
            elif len(l1) > len(l2):
                if l1[x] >= 10:
                    st1 += str(l1[x] % 10)
                    if x < len(l1) - 1:
                        l1[x + 1] += 1
                    else:
                        st1 += str(1)
            else:
                if l2[x] >= 10:
                    st1 += str(l2[x] % 10)
                    if x < len(l2) - 1:
                        l2[x + 1] += 1
                    else:
                        st1 += str(1)

        new = []
        for x in st1:
            new.append(int(x))
        return new
# Definition for singly-linked list.
 #class ListNode:
 #    def __init__(self, val=0, next=None):
 #        self.val = val
 #        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        current = dummy
         
        carrier = 0
        while l1 or l2 or carrier:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0
            value = value1 + value2 + carrier
            carrier = value // 10
            value = value % 10
            current.next = ListNode(value)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
