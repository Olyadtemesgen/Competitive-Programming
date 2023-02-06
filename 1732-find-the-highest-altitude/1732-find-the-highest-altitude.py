class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        x = 0
        result = 0
        for pt in gain:
            x += pt
            result = max(x, result)
            
        return result