class Solution:
    def findAnagrams(self, string: str, ana: str) -> list[int]:

        a = len(ana)
        b = len(string)
        dict = {}
        for x in 'qwertyuioplkjhgfdsazxcvbnm':
            dict[x] = 0
        otherd = dict.copy()
        for x in ana:
            otherd[x] += 1
        r = 0
        l = 0
        result = []
        while r < b:
            if r - l < a:
                dict[string[r]] += 1
                r += 1
            else:
                dict[string[l]] -= 1
                l += 1
            if dict == otherd:
                result.append(l)
        return result
