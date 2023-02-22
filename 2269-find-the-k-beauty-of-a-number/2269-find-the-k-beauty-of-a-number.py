class Solution:
    
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        number = num
        num = str(num)
        answer = 0
        
        if not k:
            return 0
        
        left = 0
        while k < len(num) + 1:
            
            if int(num[left:k]) and not number % int(num[left:k]):
                answer += 1
            
            k += 1
            left += 1
        
        return answer