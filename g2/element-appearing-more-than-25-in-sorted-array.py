class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        length = len(arr)
        counter = Counter(arr)

        for key in counter:
            if counter[key] / length > 0.25:
                return key