from collections import Counter


class Solution:
    def longestOnes(self, nums, k: int) -> int:
        left = 0
        right = 2
        temp = []
        while left < len(nums) and right <= len(nums):
            count = Counter(nums[left:right])
            if count[0] <= k:
                temp.append(len(nums[left:right]))
                right += 1
            else:
                left += 1
        print(temp)
        return max(temp)
    def longestOnes2(self, nums, k):
        left = 0
        maxx = 0
        for r, n in enumerate(nums):
            k -= (1 - n)
            if k < 0:
                k += (1 - nums[left])
                left += 1
            maxx = max(maxx, r - left + 1)
        return maxx
