#I did not do it all some of them are from google
class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        result = [-1] * 3
        lensubarray = len(nums) - k + 1
        otherss = [0] * lensubarray
        otherresult = 0
        for i, num in enumerate(nums):
            otherresult += num
            if i >= k:
                otherresult -= nums[i - k]
            if i >= k - 1:
                otherss[i - k + 1] = otherresult
        left = [0] * lensubarray
        maxIndex = 0
        for i in range(lensubarray):
            if otherss[i] > otherss[maxIndex]:
                maxIndex = i
            left[i] = maxIndex

        right = [0] * lensubarray
        maxIndex = lensubarray - 1

        for i in reversed(range(lensubarray)):
            if otherss[i] >= otherss[maxIndex]:
                maxIndex = i
            right[i] = maxIndex
        for i in range(k, lensubarray - k):
            if result[0] == -1 or otherss[left[i - k]] + otherss[i] + otherss[right[i + k]] > otherss[result[0]] + otherss[result[1]] + otherss[result[2]]:
                result = [left[i - k], i, right[i + k]]

        return result
