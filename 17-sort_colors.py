class Solution:
    def sortColors(self, nums):
        n0 = []
        n1 = []
        n2 = []
        for x in nums:
            if x == 0: 
                n0.append(x)
            elif x == 1:
                n1.append(x)
            else:
                n2.append(x)
        return n0 + n1 + n2
