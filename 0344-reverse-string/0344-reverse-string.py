class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        
#         while left < right:
            
#             s[left], s[right]= s[right], s[left]
#             right -= 1
#             left += 1
        
        def reverser( left, right):
            
            if right - left >= 1:
                
                s[right], s[left] = s[left], s[right]
                reverser(left + 1, right - 1)
        
        reverser(left,right)