class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums = list(map(str, nums))

        answer = ""

        for i in range(len(nums)):

            nn = nums[i]
            jj = i
            
            for j in range(i + 1, len(nums)):
                if nn + nums[j] < nums[j] + nn:
                    nn = nums[j]
                    jj = j
            
            nums[i], nums[jj] = nums[jj], nums[i]

            answer = answer + nums[i]
        
        return str(int(answer))

