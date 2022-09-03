class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        new_l =[0] * (len(nums))
        for x in range(len(nums)):
            for y in nums:
                if nums[x] > y:
                    new_l[x] += 1
        return new_l
