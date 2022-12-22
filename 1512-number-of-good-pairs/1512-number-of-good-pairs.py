class Solution:
    def numIdenticalPairs(self, nums):
        counter = 0
        for x in range(len(nums)):
            for y in range(x + 1,len(nums),1):
                if nums[x] == nums[y]:
                    counter += 1
        return counter