class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        dictt = {0:sum(nums) - nums[0]}
        dictt2 = {0:0}
        if not sum(nums[1:]):
            return 0
        for x in range(1, len(nums) - 1):
            dictt[x] = dictt[x - 1] - nums[x]
            dictt2[x] = dictt2[x - 1] + nums[x - 1]
            if dictt[x] == dictt2[x]:
                return x
        if not sum(nums[:len(nums) - 1]):
            return len(nums) - 1
        else:
            return -1
