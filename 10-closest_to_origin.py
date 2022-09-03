from math import sqrt
class Solution(object):
    def kClosest(self, points, k):
        new_a = []
        for x in range(len(points)):
            new_a.append(sqrt(points[x][0]**2 + points[x][1]**2))
        arr = new_a.copy()
        arr.sort()
        new = arr[:k]
        neww = []
        for x in new:
            neww.append(points[new_a.index(x)])
        return neww
