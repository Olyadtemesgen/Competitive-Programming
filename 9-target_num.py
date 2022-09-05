class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        new = []
        for x in range(len(nums)):
            if target == nums[x]:
                new.append(x)
        return new
