class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        answer = []
        bottom = 0
        f = firstList.copy()
        s = secondList.copy()

        for top in range(len(firstList)):

            while bottom < len(s) and s[bottom][1] < f[top][0]:
                bottom += 1
            
            ff = True
            while bottom < len(s) and (f[top][0] <= s[bottom][0] <= f[top][1] or s[bottom][0] <= f[top][0] <= s[bottom][1]):

                first = max(s[bottom][0], f[top][0])
                second = min(s[bottom][1], f[top][1])

                answer.append([first, second])
                ff = False
                bottom += 1
            
            if not ff:
                bottom -= 1

        return answer