class Solution:
    
    def sumSubarrayMins(self, arr: list[int]) -> int:
        
        monotonic = []
        result = 0
        mon_result = []

        for right in range(len(arr)):
            
            if not monotonic:
                monotonic.append(right)
                result += arr[right]
                mon_result.append(arr[right])
            
            else:
                while monotonic and arr[right] <= arr[monotonic[-1]]:
                    monotonic.pop()
                    mon_result.pop()
                
                if not mon_result:
                    mon_result.append(arr[right] * (right + 1))
                
                else:
                    mon_result.append((right - monotonic[-1]) * arr[right] + mon_result[-1]) 
                
                monotonic.append(right)
                result += mon_result[-1]
        return result % (10 ** 9 + 7)
    