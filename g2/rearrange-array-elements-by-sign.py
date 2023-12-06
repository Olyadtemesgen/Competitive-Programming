class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        positive = [i for i in nums if i >= 0]
        negative = [i for i in nums if i < 0]

        answer = []

        for index in range(len(nums) // 2):
            answer.extend([positive[index], negative[index]])
        
        return answer