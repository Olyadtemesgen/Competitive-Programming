class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:

     
        result = sum(weights)

        def isPossible(mid):
            number_of_days_required = 1
            the_sum = mid

            for weight in weights:
                
                if the_sum - weight < 0:
                    the_sum = mid
                    number_of_days_required += 1
                
                the_sum -= weight
            
            return number_of_days_required <= days
        
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = left + (right - left) // 2
            
            if isPossible(mid):

                result = min(result, mid)
                right = mid - 1
            
            else:
                left = mid + 1
            
        return result