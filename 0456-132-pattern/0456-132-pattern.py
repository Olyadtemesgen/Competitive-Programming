class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
            
            if len(nums) < 3:
                return False
            
            right = float('-inf')
            stack = []
            
            for i in range(len(nums)-1, -1, -1):
                
                if nums[i] < right:
                    return True
                
                else:
                    while stack and stack[-1] < nums[i]:
                        right = stack.pop()
                stack.append(nums[i])
            
            return False