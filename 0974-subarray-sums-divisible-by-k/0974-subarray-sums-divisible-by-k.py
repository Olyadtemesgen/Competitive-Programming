class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dictionary, prefix, result= {0:1}, 0, 0
        
        for right in nums:
            
            prefix = (prefix + right) % k
            
            result += dictionary.get(prefix, 0)
            
            dictionary[prefix] = dictionary.get(prefix, 0) + 1
        
        return result