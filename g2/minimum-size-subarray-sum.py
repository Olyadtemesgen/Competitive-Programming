class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        
        left = 0
        length = len(nums)
        minn = float('inf')
        sum = 0
        
        for right in range(length):
            sum += nums[right]
            if sum >= target:
                while sum >= target:
                    sum -= nums[left]
                    left += 1
                minn = min(right - left + 2, minn)
        
        if minn == float('inf'):
            return 0
        
        return minn