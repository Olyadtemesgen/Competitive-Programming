class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        
        answer = 0
        
        # nums.sort(reverse=True)
        
        for num in nums:
            answer |= num
        
        result = 0
        
        def find_all(index, array, anss):
            
            nonlocal result
            nonlocal answer
            
                
            if index == len(nums):
                
                if find_or(array) == answer:
                    result += 1
                
                return
            
            
                
            arr2 = array.copy()
            arr2.append(nums[index])
            
            find_all(index + 1, arr2, anss)
            
            find_all(index + 1, array, anss)
        
        def find_or(array):
            
            ans = 0
            
            for x in array:
                ans |= x
            
            return ans
        
        find_all(0, [], 0)
        
        return result
        
        