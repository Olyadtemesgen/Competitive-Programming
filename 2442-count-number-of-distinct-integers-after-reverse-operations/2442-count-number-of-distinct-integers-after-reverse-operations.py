class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        
        length = len(nums)
        index = 0
        while index < length:
            
            reverse = int(str(nums[index])[::-1])
            nums.append(reverse)
            
            index += 1
        
        return len(set(nums))