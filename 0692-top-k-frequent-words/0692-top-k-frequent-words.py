class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        dicts = defaultdict(int)
    
        for x in words: 
            dicts[x] += 1
        
        results = []
        
        for key, val in dicts.items():
            results.append([val, key])
        
        results.sort(reverse=True)
            
        result = []
        
        index = 0
        while index < k:
            
            curr_val = results[index][0]
            
            val = []
            while index < len(results) and curr_val == results[index][0]:
                
                val.append(results[index][1])
                index += 1
            
            val.reverse()
            
            if index <= k:
                result.extend(val)
            
            elif index > k:
                while index > k:
                    val.pop()
                    index -= 1
                
                result.extend(val)
        return result