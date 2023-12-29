from collections import defaultdict
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        L = len(arr2)
        d = defaultdict(lambda : L)
        for i,n in enumerate(arr2):
            d[n] = i
        arr1.sort(key=lambda x: (d[x],x))
        return arr1
        
        