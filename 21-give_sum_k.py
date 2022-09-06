class Solution:
    def maxOperations(self, nums, k):
        res = 0
        dict = {}
        for x in nums:
            if k - x  in dict and dict[k - x] > 0:
                res += 1
                dict[k - x] -= 1
            else:
                if x not in dict:
                    dict[x] = 0
                dict[x] += 1
        return res
