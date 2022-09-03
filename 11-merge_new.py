class Solution:
    def merge(self, intervals):
        count = 0
        for nums in range(len(intervals)):
            for y in range(len(intervals)):
                if intervals[nums][0] < intervals[y][0] and intervals[nums][1] >= intervals[y][0]:
                    new = [intervals[nums][0] , max(intervals[nums][1] , intervals[y][1])]
                    intervals[y] = [0  , 0]
                    intervals[nums] = [0, 0]
                    intervals.append(new)
                    count += 1
        del intervals[:count + 1]
        intervals.sort()
        return intervals
