# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        left = 1
        right = n

        while left <= right:
            mid = (left + right) / 2

            if left == right:
                return right
            
            elif isBadVersion(mid):
                right = mid
            
            else:
                left = mid + 1