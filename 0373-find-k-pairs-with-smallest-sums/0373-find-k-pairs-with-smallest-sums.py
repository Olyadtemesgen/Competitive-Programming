from heapq import *
class Solution:

    def kSmallestPairs(self, nums1, nums2, k):

        if not nums1 or not nums2:
            return []

        visited = set()
        heap = []
        answer = []

        heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited.add((0, 0))

        while len(answer) < k and heap:

            The_vals = heappop(heap)
            answer.append((nums1[The_vals[1]], nums2[The_vals[2]]))

            if The_vals[1] + 1 < len(nums1) and (The_vals[1] + 1, The_vals[2]) not in visited:
                heappush(heap, (nums1[The_vals[1] + 1] + nums2[The_vals[2]], The_vals[1] + 1, The_vals[2]))
                visited.add((The_vals[1] + 1, The_vals[2]))

            if The_vals[2] + 1 < len(nums2) and (The_vals[1], The_vals[2] + 1) not in visited:
                heappush(heap, (nums1[The_vals[1]] + nums2[The_vals[2] + 1], The_vals[1], The_vals[2] + 1))
                visited.add((The_vals[1], The_vals[2] + 1))

        return answer