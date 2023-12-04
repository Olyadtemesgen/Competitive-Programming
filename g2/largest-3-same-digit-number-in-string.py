class Solution:
    def largestGoodInteger(self, nums: str) -> str:
        
        index = 0
        answer = ""
        while  index < len(nums) - 2:

            idx = index
            ff = False
            
            while idx < len(nums) - 1 and idx < index + 2:
                
                if nums[idx] != nums[idx + 1]:
                    ff = True
                    index = idx + 1
                    break
                
                else:
                    idx += 1
                
                if idx == index + 2:
                    index = index + 3

                    if len(answer) == 3:
         
                        if int(nums[idx]) > int(answer[0]):
                            
                            answer = nums[idx] * 3
                    
                    else:
                        answer = nums[idx] * 3

        return answer