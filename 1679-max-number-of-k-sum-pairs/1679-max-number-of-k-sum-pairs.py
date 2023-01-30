class Solution:
    def maxOperations(self, nums, k):
        res = 0
        dict = {}
        for abc in nums:
            dict[abc] = 0
        for x in nums:
            
            if k - x  in dict and dict[k - x] > 0:
                res += 1
                
                dict[k - x] -= 1
            
            else:
                dict[x] += 1
        
        return res