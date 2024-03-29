import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        
        left = 1
        
        right = max(piles)
        
        result = right
        
        while left <= right:

            mid = left +  (right - left) // 2
            
            total_hours_required = 0
            
            for pile in piles:
                
                total_hours_required += max(1, math.ceil(pile / mid))
            
            if total_hours_required <= h:
                
                result = min(result, mid)
                right = mid - 1
            
            else:
                left = mid + 1
        
        return result