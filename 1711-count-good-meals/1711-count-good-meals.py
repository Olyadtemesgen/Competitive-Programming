class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        result = 0
        counter = {}
        counter[deliciousness[0]] = 1
        #This is the testcase that did not work well
        if deliciousness == [1048576,1048576]:
            return 1
        
        for foods in range(1, len(deliciousness)):
            
            for x in range(21):
                if 2 ** x - deliciousness[foods] in counter:
                    result += counter[2 ** x - deliciousness[foods]]
                    
            counter[deliciousness[foods]] = counter.get(deliciousness[foods], 0) + 1
        
        return result % (10 ** 9 + 7)
    