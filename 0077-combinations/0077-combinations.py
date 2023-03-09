class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        result = []
        
        array = [x for x in range(1, n + 1)]
        
        def conbinator(index, array, arr):
            
            nonlocal result
            
            if len(arr) == k:
                result.append(arr)
                arr = []
                return
            
            if index == n:
                arr = []
                return
            
            
            arr.append(array[index])
            arr2 = arr.copy()
            conbinator(index + 1, array, arr2)
            
            arr.pop()
            
            conbinator(index + 1, array, arr)
        
        conbinator(0, array, [])
        
        result.sort()
        
        return result
        