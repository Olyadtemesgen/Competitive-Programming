class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        ranges.sort()
        for start, end in ranges:
            if start <= left:
                left = max(left, end + 1)
        
        return left > right