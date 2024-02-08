class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        answer = []
        length = len(nums)

        for index in range(len(nums)):
            number = prefix[-1] - prefix[index] - ((length - index - 1) * nums[index])
            number += abs(prefix[index] - nums[index] * (index + 1))
            answer.append(number)
        
        return answer