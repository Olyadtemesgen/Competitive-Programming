class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        
        i = -1
        answer = 0
        for ii in range(len(flips)):
            i = max(i , flips[ii])
            if i == ii + 1:
                answer += 1
        
        return answer
