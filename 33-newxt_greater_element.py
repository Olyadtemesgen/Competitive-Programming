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
#this is the best algorithm and it is beautiful man
    def nextGreaterElement2(self, nums1, nums2):
        indexer = {j:i for i, j in enumerate(nums1)}
        result = [0] * len(nums1)
        stack = []
        for x in range(len(nums2)):
            current = nums2[x]
            while stack and current > stack[-1]:
                value = stack.pop()
                nums = indexer[value]
                result[nums] = current
            if current in nums1:
                stack.append(current)
        return result
