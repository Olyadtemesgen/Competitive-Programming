class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        hashprefixmap = {0:1}
        prefixsum, result = 0, 0
        for x in range(len(nums)):
            prefixsum += (nums[x] % 2)
            result += hashprefixmap.get(prefixsum - k, 0)
            hashprefixmap[prefixsum] = 1 + hashprefixmap.get(prefixsum, 0)
        return result
