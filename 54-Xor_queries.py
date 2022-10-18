class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        #first find the prefix of Xor
        prefix = 0
        prefix = [0] * (len(arr) + 1)
        result = []
        for x in range(len(arr)):
            prefix[x + 1] = prefix[x] ^ arr[x]
        for l, r in queries:
            result.append(prefix[l] ^ prefix[r + 1])
        return result
