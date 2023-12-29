class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        
        arr = list(set(nums1).intersection(set(nums2)))
        
        arr2 = []
        
        for x in arr:
            
            for a in range(min(nums1.count(x), nums2.count(x))):
                arr2.append(x)
        return arr2