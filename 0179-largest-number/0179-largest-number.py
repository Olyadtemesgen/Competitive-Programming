import functools
class Solution:
    def largestNumber(self, nums):
        
        return str(int("".join(sorted(list(map(str, nums)), key=functools.cmp_to_key(lambda a, b:-1 if a + b > b + a else 1 )))))