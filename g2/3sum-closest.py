class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        result = sum(nums[:3])
        res = abs(sum(nums[:3]) - target)
        for point in range(len(nums) - 2):
            left = point + 1
            right = len(nums) - 1
            while right > left:
                if res > abs(nums[point] + nums[left] + nums[right] - target):
                    res =  abs( nums[point] + nums[left] + nums[right] - target)
                    result = nums[point] + nums[left] + nums[right]
                if nums[point] + nums[right] + nums[left] > target:
                    right -= 1
                elif nums[point] + nums[right] + nums[left] < target:
                    left += 1
                elif nums[point] + nums[right] + nums[left] == target:
                    return target
        return result