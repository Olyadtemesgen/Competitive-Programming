class Solution:
    def kthLargestNumber(self, nums , key):
        new = []
        for nu in nums:
            new.append(int(nu))
        new.sort()
        new.reverse()
        return str(new[key - 1])
