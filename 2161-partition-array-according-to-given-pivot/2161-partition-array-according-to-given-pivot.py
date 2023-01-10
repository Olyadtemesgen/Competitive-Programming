class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        index1 = []
        index2 = []
        index3 = []
        
        for num in nums:
            if num < pivot:
                index1.append(num)
            
            elif num > pivot:
                index3.append(num)
                
            else:
                index2.append(num)
        
        return index1 + index2 + index3