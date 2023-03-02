class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        #This is a better Code I think and It
        from collections import deque
        stack = []
        
        result = [-1] * len(nums)

        length = len(nums)
        nums = nums + nums
        for right in range(len(nums)):
            
            rights = right % length

            while stack and nums[right] > nums[stack[-1]]:
                result[stack.pop()] = nums[right]
            
            if not stack or stack[-1] != rights:
                stack.append(rights)
        
      
        return result

#This is the second code        
        stackvalue = []
        stackindex = []
        result = 0
        results = [None] * len(nums)
        
        for index, num in enumerate(nums):
            
            if not stackvalue or stackvalue[-1] >= num:
                stackvalue.append(num)
                stackindex.append(index)
            
            elif stackvalue[-1] < num:
                
                while stackvalue and stackvalue[-1] < num:
                    results[stackindex.pop()] = num
                    stackvalue.pop()
                
                stackindex.append(index)
                stackvalue.append(num)
        
        for num in nums:
            
            if num > nums[-1]:
                results[-1] = num
                break
        
        for index, num in enumerate(results):
            
            if num == None:
                
                for nu in nums[:index]:
                    
                    if nu > nums[index]:
                        results[index] = nu
                        break
        
        for index, num in enumerate(results):
            
            if num == None:
                results[index] = -1
        
        return results