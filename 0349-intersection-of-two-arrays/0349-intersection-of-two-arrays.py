class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        aa = set(nums1)
        
        bb = set(nums2)
        
        return list(aa.intersection(bb))