class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums1 = []
        nums2 = []
        
        for index, num in enumerate(nums):
            if index == 0 and num > 0:
                positive = 0
            
            elif index == 0:
                negative = 0
                
            if num > 0:
                nums1.append(num)
            else:
                nums2.append(num)
        positive = 0    
        while positive < len(nums):
            
            nums[positive] = nums1[positive // 2]
            nums[positive + 1] = nums2[positive // 2]
            positive += 2
        return nums