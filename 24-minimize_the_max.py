class Solution:
    def minPairSum(self, nums):
        nums.sort()
        smaller = 0
        larger = len(nums) - 1
        new = []
        while larger >= smaller:
            new.append(nums[larger] + nums[smaller])
            larger -= 1
            smaller += 1
        return max(new)
