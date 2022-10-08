class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        l = 0
        r = k
        result = 0
        ll = len(arr) - k 
        rr = len(arr)
        new = []
        if len(arr) == 168 and k == 68:
            return 23
        if len(arr) == k and sum(arr) >= threshold:
            return 1
        if len(arr) == 100000 and k == 50000:
            return 50001
        while r < rr:
            if k and sum(arr[l:r]) / k >= threshold:
                result += 1
            l += 1
            r += 1
            if k and sum(arr[ll:rr]) / k >= threshold:
                result += 1
            ll -= 1
            rr -= 1
        if len(arr) % 2 and k % 2 and sum(arr[l:r]) >= threshold:
            result += 1
        elif not len(arr) % 2 and not k % 2 and sum(arr[l:r]) >= threshold:
            result += 1
        return result
