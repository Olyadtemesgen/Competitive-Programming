class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        down = [[trips[i][2], trips[i][0]] for i in range(len(trips))]
        up = [[trips[i][1], trips[i][0]] for i in range(len(trips))]

        up.sort()
        down.sort()

        down_p = 0

        current = 0
        for up_p in range(len(trips)):
            current += up[up_p][1]
            while down_p < len(trips) and down[down_p][0] <= up[up_p][0]:
                current -= down[down_p][1]
                down_p += 1
            
            if current > capacity:
                return False
            
        return True
            
