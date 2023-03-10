class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = [[]]
        
        def subset(arr, index):
            
            if arr not in result:
                result.append(arr)
            
            if index == len(nums):
                return
            
            arr2 = arr.copy()
            arr.append(nums[index])
            
            subset(arr2, index + 1)
            
            subset(arr, index + 1)
        
        subset([], 0)
        
        return result