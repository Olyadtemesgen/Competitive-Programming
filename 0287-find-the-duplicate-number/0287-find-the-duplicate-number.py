class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for count, aa in counter.items():
            if aa >= 2:return count