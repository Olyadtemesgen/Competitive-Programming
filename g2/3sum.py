class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        left = 0

        answer = []
        for x in range(len(nums) - 2):

            l = x + 1
            r = len(nums) - 1

            while l < r:
                if nums[x] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[x] + nums[l] + nums[r] < 0:
                    l += 1
                
                elif [nums[x], nums[l], nums[r]] not in answer:
                    answer.append([nums[x], nums[l], nums[r]])
                    l += 1
                    r -= 1
                
                else:
                    l += 1
                    r -= 1
        return answer