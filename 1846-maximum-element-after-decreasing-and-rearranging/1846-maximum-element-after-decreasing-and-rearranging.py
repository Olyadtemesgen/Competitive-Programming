class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        arr.sort()
        
        arr[0] = 1
        
        for index in range(1, len(arr)):
            if arr[index] - arr[index - 1] > 1:
                arr[index] = arr[index - 1] + 1
        
        return len(Counter(arr))