class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        right = len(arr) - 1
        left = 0
        
        while left <= right:
            
            mid = (left + right) // 2
            
            if mid and arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            
            elif mid == 0:
                return 1
            elif arr[mid - 1] < arr[mid] < arr[mid + 1]:
                left = mid + 1
            
            else:
                right = mid - 1