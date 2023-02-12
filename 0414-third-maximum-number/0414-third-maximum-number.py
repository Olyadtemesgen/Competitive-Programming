class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        array = sorted(list(set(nums)))
        return array[-1] if len(array) < 3 else array[-3]