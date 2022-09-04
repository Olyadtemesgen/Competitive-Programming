import functools
class Solution:
    def largestNumber(self, nums):
        new = []
        for x in nums:
            new.append(str(x))
        numss = sorted(new, key=functools.cmp_to_key(lambda a, b:-1 if a + b > b + a else 1 ))
        return str(int("".join(numss)))
