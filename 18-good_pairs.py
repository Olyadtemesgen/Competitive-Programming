from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums):
        counter = Counter(nums)
        numss = 0
        for x in set(nums):
            if counter[x] > 1:
                numss += (counter[x] * (counter[x] - 1)) // 2
        return numss
      #it is also possible to use this one
     def numIdenticalPairs2(self, nums):
        counter = 0
        for x in range(len(nums)):
            for y in range(x + 1,len(nums),1):
                if nums[x] == nums[y]:
                    counter += 1
        return counter
