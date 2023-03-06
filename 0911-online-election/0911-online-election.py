
class TopVotedCandidate:
    
    def __init__(self, persons: list[int], times: list[int]):
        from collections import defaultdict
        
        self.persons = persons
        self.times = times
        self.size = len(times)
        
        self.counter = defaultdict(int)
        maximum = self.persons[0]

        for indexs in range(self.size):
            self.counter[self.persons[indexs]] += 1
            
            if self.persons[indexs] != maximum and self.counter[maximum] <= self.counter[self.persons[indexs]] :
                
                maximum = self.persons[indexs]
                self.persons[indexs] = maximum
            
            else:
                self.persons[indexs] = maximum
        
    def q(self, t: int) -> int:

        left = 0
        right = self.size - 1
        
        while left <= right:
            mid = left + (right - left) // 2
        
            if mid != self.size - 1:
                if  self.times[mid] <= t and self.times[mid + 1] > t:
                    return self.persons[mid]

            else:
                return self.persons[-1]
            
            if self.times[mid] > t:
                right = mid 
            
            elif self.times[mid] < t and self.times[mid - 1] < t:
                left = mid + 1

# aa = TopVotedCandidate([0,0,0,0,1],[0,6,39,52,75])
# print(aa)
# print(aa.q(68))
# # ["TopVotedCandidate","q","q","q","q","q","q","q","q","q","q"]
# # S[[[0,0,0,0,1],[0,6,39,52,75]],[45],[49],[59],[68],[42],[37],[99],[26],[78],[43]]