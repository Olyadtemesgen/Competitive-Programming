# class Solution:
#     def countSubarrays(self, nums: List[int], k: int) -> int:
#         result = 0
#         prefix = [nums[0]]
#         for index in nums[1:]:
#             prefix.append(index + prefix[-1])
#         for index1 in range(len(nums)):
#             for index2 in range(index1, len(nums)):
#                 if index1 == 0:
#                     if (index2 - index1 + 1) * (prefix[index2]) < k:result += 1
#                 elif (index2 - index1 + 1) * (prefix[index2] - prefix[index1 - 1]) < k:
#                     result += 1
#                 else:break
#         return result
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        left = 0
        product = 0
        answer = 0
        
        for right in range(len(nums)):
            if product:
                product = (product / (right - left) +  nums[right]) * (right - left + 1)
            
            else:
                product = nums[right]
                
            
            while left <= right and product >= k:
                
                product = (product / (right - left + 1) - nums[left]) * (right - left)
                
                left += 1
            
            answer += (right - left + 1)
        
        return answer