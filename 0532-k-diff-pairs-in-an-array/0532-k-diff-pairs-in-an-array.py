class Solution:

    def findPairs(self, nums: List[int], k: int) -> int:

        dictionary = defaultdict(int)
        result = 0
        res = []
        for right in nums:
            

            if k + right in dictionary and (right, k + right) not in res:
                result += 1
                res.append((min(right, k + right), max(right, k + right)))
            
            if right - k in dictionary and (right - k, right) not in res:
                result += 1
                res.append((min(right, right - k), max(right, right - k)))

            dictionary[right] += 1
            
        return result