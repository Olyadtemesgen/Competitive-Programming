class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort(reverse=True)
        
        for i in range(len(nums) - 2):
            
            one = nums[i]
            
            two = nums[i+1]
            
            three = nums[i+2]
            if three + two > one:
                return one + two + three
        
        return 0