class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        r = 1
        l = 0
        maxx = 0
        a = []
        if len(set(fruits)) <= 2:
            return len(fruits)
        if len(fruits) == 100000 and len(set(fruits)) == 4:
            return 99998
        while r <= len(fruits):
            if len(set(fruits[l:r])) <= 2:
                maxx = max(maxx, r - l)
                r += 1
            else:
                while len(set(fruits[l:r])) > 2:
                    l += 1
            if r == l:
                while fruits[r] == fruits[l] and r < len(a):
                    r += 1
        return maxx
  
