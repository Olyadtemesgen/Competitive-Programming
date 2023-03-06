class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        counter = {}
        for index in range(len(arr)):
            
            if arr[index] * 2 in counter or arr[index] / 2 in counter:
                return True
            
            counter[arr[index]] = index
        
        return False
            