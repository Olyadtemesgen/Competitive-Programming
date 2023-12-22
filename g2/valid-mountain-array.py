class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        flag = True
        if len(arr) < 3:
            return False
        for index, num in enumerate(arr[1:]):
            
            
            if (not flag and num >= arr[index]) or num == arr[index]:
                return False
                        
            if flag and num < arr[index] and index == 0:
                return False
            
            if flag and num < arr[index]:
                
                flag = False

            
        return not flag