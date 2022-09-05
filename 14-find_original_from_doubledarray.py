#this has O(n^2) time complexity and not efficient
from collections import Counter
import random
class Solution:
    def findOriginalArray(self, changed):
        new = []
        for nums in random.sample([abc for abc in range(1000000)],1):
            if nums not in changed:
                changer = nums
                break
        for x in range(len(changed)):
            for y in changed:
                if changed[x] * 2 == y:
                    new.append(changed[x])
                    changed[changed.index(y)] = changer
        if len(new) == len(changed) // 2 and len(new) % 2 == 0:
            return new
        else:
            return []
     #the more efficient one is
     def findOriginalArray2(self, changed):
     
     
