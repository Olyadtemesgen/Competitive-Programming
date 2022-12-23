class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for x in range(len(nums1) - 1, -1, -1): 
            if n == 0:
                break
                
            elif m == 0:
                nums1[:n] = nums2[:n]
                break
            if nums1[m - 1] > nums2[n - 1]:
                nums1[x] = nums1[m - 1]
                m -= 1

            else:
                nums1[x] = nums2[n - 1]
                n -= 1
        return nums1
        nums1[:] = nums1
        print(nums1)














# we also can solve this by using this

        # stack = []
        # pright = 0

        # for ileft in range(m):
        #     if pright == n:
        #         if stack and stack[0] < nums1[ileft]:
        #             stack.append(nums1[ileft])
        #             nums1[ileft] = stack[0]

        #             del stack[0]

        #     elif nums1[ileft] > nums2[pright]:
        #         if stack and stack[0] <= nums2[pright]:
        #             stack.append(nums1[ileft])
        #             nums1[ileft] = stack[0]

        #             del stack[0]

        #         else:
        #             stack.append(nums1[ileft])
        #             nums1[ileft] = nums2[pright]
        #             pright += 1

        #     elif stack and stack[0] < nums1[ileft]:
        #         stack.append(nums1[ileft])
        #         nums1[ileft] = stack[0]

        #         del stack[0]

        # x = m
        # while stack and pright < len(nums2):
        #     if stack[0] <= nums2[pright]:
        #         nums1[x] = stack[0]
                
        #         del stack[0]

        #     else:
        #         nums1[x] = nums2[pright]
        #         pright += 1

        #     x += 1

        # if stack:
        #     nums1[x:] = stack

        # elif pright < len(nums2):
        #     nums1[x:] = nums2[pright:]

        


            
                