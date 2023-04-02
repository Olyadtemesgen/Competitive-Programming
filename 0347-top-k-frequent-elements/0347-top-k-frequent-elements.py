from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        
        freq = [[] for i in range(len(nums) + 1)]
        
        counter = Counter(nums)
        
        new = []
        the = []
        
        for x in counter:
            new.append(counter[x])
            the.append(x)
        
        neww = new.copy()
        
        sorte = []
        
        for x in range(k):
            sorte.append(new.pop(new.index(max(new))))
        
        other = []
        
        for abc in sorte:
            
            other.append(the[neww.index(abc)])
            del the[neww.index(abc)]
            del neww[neww.index(abc)]
        
        return other