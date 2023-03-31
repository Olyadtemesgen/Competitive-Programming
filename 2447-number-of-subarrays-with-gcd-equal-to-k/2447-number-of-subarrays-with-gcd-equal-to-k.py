class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        result = nums.count(k)

        for x in range(len(nums)):
            
            saved = nums[x]
            
            if nums[x] >= k:

                for y in range(x + 1, len(nums)):
                    
                    if nums[y] < k or saved < k:
                        break

                    saved = math.gcd(saved, nums[y]) 
                    
                    result += saved == k

        return result