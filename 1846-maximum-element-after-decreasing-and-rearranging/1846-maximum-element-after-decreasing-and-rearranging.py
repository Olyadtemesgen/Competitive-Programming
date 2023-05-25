class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        arr.sort()
        
        arr[0] = 1
        
        for index in range(1, len(arr)):
            
            if arr[index] - arr[index - 1] > 1:
                
                arr[index] = arr[index - 1] + 1
        
        answer = 1
        
        for x in range(1, len(arr)):
            
            if arr[x] != arr[x - 1]:
                answer += 1
        
        return answer