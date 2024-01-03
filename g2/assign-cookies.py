class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        right = len(g)  - 1
        sindex = len(s) - 1
        answer = 0
        
        if not s or not g:
            return 0
        
        while right + 1 and sindex + 1:
            
            while right + 1 and g[right] > s[sindex]:
                right -= 1


            if right + 1:

                right -= 1
                sindex -= 1
                answer += 1
        return answer