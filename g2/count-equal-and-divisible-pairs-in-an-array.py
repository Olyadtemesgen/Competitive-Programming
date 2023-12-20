class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        answer = 0
        for i in range(len(nums)):
            
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and not (i *j) % k:
                    answer += 1
            
        
        return answer