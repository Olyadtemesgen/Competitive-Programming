class Solution:
    
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        answer = [0]
        for indexs in range(1, len(nums)):
            nums[indexs] += nums[indexs - 1]
        
        for index in range(len(nums)):
            
            if not index:
                answer.append(nums[index])
                
            else:
                for x in range(index + 1):

                    if not x:
                        answer.append(nums[index])

                    else:
                        answer.append(nums[index] - nums[x - 1])
        
        answer.sort()
        
        for ans in range(1, len(answer)):
            answer[ans] += answer[ans - 1]
        
        return (answer[right ] - answer[left - 1]) % (10**9 + 7)