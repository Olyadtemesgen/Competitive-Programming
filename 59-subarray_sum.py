class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefixsum = {0:1}
        sum = 0
        result = 0
        for x in range(len(nums)):
            sum += nums[x]
            if sum - k in prefixsum:
                result += prefixsum[sum - k]
            if sum in prefixsum:
                prefixsum[sum] += 1
            else:
                prefixsum[sum] = 1
        return result
