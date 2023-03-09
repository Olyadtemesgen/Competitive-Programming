class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        result = []
        
        array = [x for x in range(1, n + 1)]
        
        def conbinator(index, arr):
            
           
            
            if len(arr) == k:
                result.append(arr)
                arr = []
                return
            
            if index == n:
                arr = []
                return
            
            
            arr.append(array[index])
            arr2 = arr.copy()
            conbinator(index + 1, arr2)
            
            arr.pop()
            
            conbinator(index + 1, arr)
        
        conbinator(0, [])
        
        result.sort()
        
        return result
        