class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        b = len(cardPoints)
        length = b - k
        minn = sum(cardPoints[:length])
        left = 0
        x = minn
        while length < b:
            minn = minn - cardPoints[left] + cardPoints[length]
            x = min(x, minn)
            length += 1
            left += 1
        return sum(cardPoints) - x
