class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        prefix = [0] * len(nums)
        nums.sort(reverse=True)
        for start, end in requests:

            prefix[start] += 1
            if end < len(nums) - 1:
                prefix[end + 1] -= 1
        
        for i in range(1, len(nums)):
            prefix[i] += prefix[i - 1]
        
        prefix.sort(reverse=True)

        answer = 0

        for i in range(len(prefix)):
            answer += nums[i] * prefix[i]
        
        return answer % (10 ** 9 + 7)