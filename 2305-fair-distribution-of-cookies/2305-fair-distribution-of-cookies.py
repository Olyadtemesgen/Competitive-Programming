class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        
        cookie = [0 for x in range(k)]
        result = float("inf")
        
        def findminimum(array, index):
            
            nonlocal result
            
            if result <= max(array) or  result == max(cookies):
                return
            
            if index == len(cookies):
                
                result = min(max(array), result)
                return
            
            for x in range(k):
                
                array[x] += cookies[index]
                
                findminimum(array, index + 1)
                
                array[x] -= cookies[index]
        
        findminimum(cookie, 0)
        
        return result