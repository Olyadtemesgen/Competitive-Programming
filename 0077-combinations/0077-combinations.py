class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        result = []
        
        array = [x for x in range(1, n + 1)]
        
        def conbinator(index, arrays, arr):
            
            nonlocal result
            
            if len(arr) == k:
                result.append(arr)
                arr = []
            
            if index == n:
                arr = []
                return
            
            arr2 = arr.copy()
            arr2.append(array[index])
            
            conbinator(index + 1, arrays[index + 1:], arr2)
            conbinator(index + 1, arrays[index + 1:], arr)
        
        conbinator(0, array, [])
        
        result.sort()
        
        res = [result[0]]
        
        for x in result[1:]:
            if res[-1] != x:
                res.append(x)
                
        return res