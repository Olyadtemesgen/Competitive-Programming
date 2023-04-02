class Solution:
  
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        ans = set()
        
        for num in nums:
            
            ins = 2
            
            while num != 1 and ins <= num:
                
                if not num % ins:
                    ans.add(ins)
                    num = num // ins
                    ins = 2
                
                else:
                    ins += 1
                    
        return len(ans)