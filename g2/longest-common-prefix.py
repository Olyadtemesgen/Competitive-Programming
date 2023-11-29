class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        
   
        minn = float('inf')
        
        for x in strs:
            minn = min(minn, len(x))
        
        if len(strs) == 1:return strs[0]
        
        for x in range(minn):
            
            aa = strs[0][x]
            
            for y in range(1 , len(strs)):
                if aa != strs[y][x]:return ans
                if y == len(strs) - 1:ans += aa
        return ans