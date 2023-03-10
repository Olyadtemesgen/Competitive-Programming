class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        result = [[]]
        nums.sort()
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
         
        
        resul = []
        for res in result:
            if res not in resul:
                resul.append(res)
        return resul