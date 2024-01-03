class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        length = len(nums)
        answer = 0

        for i in range(length):
            bf = answer
            for j in range(i + 1, length):
                
                if nums[i] + nums[j] < target:
                    answer += 1

        return answer
        