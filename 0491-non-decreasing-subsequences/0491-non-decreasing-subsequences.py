class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        result = set()
        
        def to_be_returned(array, index):
            nonlocal result

            if index == len(nums):
                return  

            array2 = array.copy()
            
            if not array2 or array2[-1] <= nums[index]:
                array2.append(nums[index])
            
            if len(array2) > 1:
                result.add(tuple(array2))
                   
            to_be_returned(array2, index + 1)
          
            to_be_returned(array, index + 1)
        
        to_be_returned([], 0)
        
        return result