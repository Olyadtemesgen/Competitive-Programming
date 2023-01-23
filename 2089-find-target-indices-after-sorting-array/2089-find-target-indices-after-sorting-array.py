class Solution(object):
    def targetIndices(self, nums, target):
        sorta = sorted(nums)
        new = []
        for x in range(len(nums)):
            if target == sorta[x]:
                new.append(x)
        return new