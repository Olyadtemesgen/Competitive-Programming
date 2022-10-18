class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        x = sum(chalk)
        if x:
            a = (k / x - k // x) * x
        if a - int(a) > .1:
            a = int(a) + 1
        else:a = int(a)
        x = 0
        while a >= chalk[x] and x < len(chalk):
            a -= chalk[x]
            x += 1
        return x
