class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        a = len(nums) / 3
        res = 0
        for x, y in counter.items():
            if y > a:
                nums[res] = x
                res += 1
        return nums[:res]
                