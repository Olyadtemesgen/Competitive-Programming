class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0
        
        for x in range(0, len(nums), 2):
            sum += nums[x]
        
        return sum
    #Jesus Is Lord