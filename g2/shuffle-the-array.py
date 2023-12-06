class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        index2 = len(nums) // 2
        answer = []

        for i in range(len(nums) // 2):
            answer.extend([nums[i], nums[i + index2]])
        
        return answer