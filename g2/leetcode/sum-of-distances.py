class Solution:
    def distance(self, nums: List[int]) -> List[int]:    

        indexes = defaultdict(list)

        prefix = defaultdict(list)
        
        for i in range(len(nums)):
            indexes[nums[i]].append(i)
            prefix[nums[i]].append(0)
        
        answer = [0] * len(nums)
        for key in indexes:
            
            leng = len(indexes[key])
            if leng > 1:
                
                first = 0
                ff = indexes[key][0]
                for i in indexes[key]:
                    first += i - ff
                
                answer[ff] = first
                prefix[key][0] = first

                for i in range(1, leng):
                    before = prefix[key][i - 1]

                    difference = indexes[key][i] - indexes[key][i - 1]

                    before += (difference * (i - 1))

                    before -= (difference * (leng - i - 1))

                    prefix[key][i] = before
                    answer[indexes[key][i]] = before
        
        return answer