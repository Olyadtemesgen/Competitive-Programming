from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        answer_taker = SortedList([nums[-1]])

        result =  [0]
        for x in range(len(nums) - 2, -1, -1):
            
            saved = bisect.bisect_left(answer_taker, nums[x])
            
            result.append(saved)
            
            answer_taker.add(nums[x])
        
        result.reverse()
        
        return result


        # total = 0
        # array = []

        # answer = [ 0 for x in range(len(nums))]

        # def merger(left, right):
            
        #     nonlocal answer
            
        #     if left - right == -1:
        #         return [left]
            
        #     elif left >= right:
        #         return []

        #     mid = left + (right - left) // 2

        #     righter = merger(mid, right)
            
        #     mid = left + (right - left) // 2
            
        #     lefter = merger(left, mid)
            
        #     leftt = 0
        #     rightt = 0

        #     result = []
        #     other = []

        #     for number in lefter:
                
        #         while  rightt < len(righter) and nums[number] >= nums[righter[rightt]]:    
        #             result.append(righter[rightt])
        #             other.append(nums[righter[rightt]])
        #             leftt += 1
        #             rightt += 1
                
                        
                
        #         answer[number] = bisect.bisect_left(other,nums[number])
        #         result.append(number)
        #         other.append(nums[number]) 
                
        #     while rightt < len(righter):
                
        #         # other.append(nums[righter[rightt]])
        #         result.append(righter[rightt])
        #         rightt += 1
            
        #     return result
        
        # merger(0, len(nums))
        
        # return answer