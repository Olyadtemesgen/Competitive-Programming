class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        ones = [nums[-1]] * len(nums)
        zeros = [1 - nums[0]] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            ones[i] = ones[i + 1] + nums[i]
        
        # ones.reverse()
        for j in range(1, len(nums)):
            zeros[j] = zeros[j - 1] + 1 - nums[j]
        
        maximum = 0


        for index in range(len(nums) + 1):

            if not index:
                maximum = ones[0]
            
            elif index == len(nums):
                maximum = max(maximum, zeros[index  - 1])
            
            else:
                maximum = max(maximum, zeros[index - 1] + ones[index])
    
        answer = []

        
        for indx in range(len(nums) + 1):
            if not indx:
                if ones[indx] == maximum:
                    answer.append(0)
            
            elif indx == len(nums):
                if zeros[indx - 1] == maximum:
                    answer.append(indx)
            
            elif zeros[indx - 1] + ones[indx] == maximum:
                answer.append(indx)

        return answer