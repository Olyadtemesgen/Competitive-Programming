class NumArray:

    def __init__(self, nums: List[int]):
        
        self.nums = nums
        self.prefix = [self.nums[0]]
        
        for num in self.nums[1:]:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        if not left:
            return self.prefix[right]
        
        return self.prefix[right] - self.prefix[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
