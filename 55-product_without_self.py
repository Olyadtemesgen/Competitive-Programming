class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        arr = [nums[0]]
        product = nums[0] 
        for x in range(1, len(nums)):
            product *= nums[x]
            arr.append(product)
        pro2 = [nums[len(nums) - 1]] * len(nums)
        prod2 = nums[len(nums) - 1]
        for y in range(len(nums) - 2, -1, -1):
            prod2 *= nums[y]
            pro2[y] = prod2
        finala = [pro2[1]]
        for x in range(1, len(nums) - 1):
            finala.append(arr[x - 1] * pro2[x + 1])
        finala.append(arr[len(nums) - 2])
        return finala
