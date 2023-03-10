class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        dictionary = {}
        
        for interval in range(len(intervals)):
            dictionary[tuple(intervals[interval])] = interval
        
        interval2 = sorted(intervals)
        result = []
        
        for index in intervals:
            saved = bisect.bisect_left(interval2, [index[1]])
            print(index, saved)
            
            if saved < len(intervals):
                result.append(dictionary[tuple(interval2[saved])])
            
            else:
                result.append(-1)
        
        return result
            