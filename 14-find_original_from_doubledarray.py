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
    #the more efficient one is and has the time complexity of O(n)
    def findOriginalArray2(self, changed):
        counter = Counter(changed)
        result = []
        for num in changed:
            if num == 0 and counter[num] >= 2:
                counter[num] -= 2
                result.append(num)
            elif  counter[num] and counter[num * 2]:
                counter[num] -= 1
                counter[num * 2] -= 1
                result.append(num)
        return result if len(result) == len(num) // 2
            
     
     
