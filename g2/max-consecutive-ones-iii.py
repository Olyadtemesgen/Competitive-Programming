class Solution:
    def longestOnes(self, nums, k):
        left = 0
        maxx = 0
        for r, n in enumerate(nums):
            k -= (1 - n)
            if k < 0:
                k += (1 - nums[left])
                left += 1
            maxx = max(maxx, r - left + 1)
        return maxx