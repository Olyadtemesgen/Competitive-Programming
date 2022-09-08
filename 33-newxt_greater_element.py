class Solution:
    def nextGreaterElement(self, nums1, nums2):
        new = []
        for x in nums1:
            k = nums2.index(x)
            for y in nums2[k:]:
                if y > x:
                    new.append(y)
                    break
            else:
                new.append(-1)
        return new
