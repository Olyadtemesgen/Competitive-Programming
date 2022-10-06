class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen: int, secondLen: int) -> int:
        left = 0
        right = max(firstLen, secondLen)
        summ = 0
        
        while right <= len(nums):
            new = sum(nums[left:right])
            te = 0
            teo = min(firstLen, secondLen)
            while teo <= len(nums):
                if teo not in range(left, right) and te not in range(left, right) and summ < new + sum(nums[te:teo]):
                    summ = new + sum(nums[te:teo]) 
                teo += 1
                te += 1 
            left += 1
            right += 1
        return summ
