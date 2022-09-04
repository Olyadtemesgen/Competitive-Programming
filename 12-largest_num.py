import functools
class Solution:
    def largestNumber(self, nums):
        new = []
        for x in nums:
            new.append(str(x))
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1 
            else:
                return 1
        numss = sorted(new, key=functools.cmp_to_key(compare))
        return str(int("".join(numss)))
