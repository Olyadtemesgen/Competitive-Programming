class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        
        index = len(arr) - 1
        
        if not index:
            return arr
        
        value = -1
        while index:
            
            if arr[index] < arr[index - 1]:
                value = index - 1
                break
            
            index -= 1
        
        if value == -1:
            return arr
        
        mins = 0
        
        for x in range(value + 1, len(arr)):
            if arr[value] > arr[x] and mins < arr[x]:
                index = x
                mins = arr[x]
        
        arr[value], arr[index] = arr[index], arr[value]
        
        return arr