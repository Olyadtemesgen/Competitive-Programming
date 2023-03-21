class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        answer = 0
        
        def char_concatenator(result, index):
            
            nonlocal answer
            
            if index == len(arr):
                return
            
            answer = max(answer, len(result))
            
            result2 = result.copy()
            
            aa = False
            counter = Counter(arr[index])
            for x in arr[index]:
                if x in result2 or counter[x] > 1:
                    aa = True
            
            
            if not aa:
                result2 += list(arr[index])
            
            answer = max(answer, len(result2))
            
            char_concatenator(result2, index + 1)
            
            char_concatenator(result, index + 1)
        
        char_concatenator([], 0)
        return answer
            