class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:

        counter = Counter(nums)

        result = 0
        rr = -1
        for c in counter:
            if not c % 2 and counter[c] > result:
                result = counter[c]
                rr = c
            
            elif not c % 2 and counter[c] == result and rr > c:
                rr = c
        
        return rr
