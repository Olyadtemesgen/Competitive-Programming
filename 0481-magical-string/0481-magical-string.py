class Solution:
    def magicalString(self, n: int) -> int:
        
        right = '1'
        
        pointer = ['1', '2']
        
        left_pointer = 0
        right_pointer = 0
        
        result = 1
        n -= 1
        flag = False
        while n:
            right += pointer[int(right[right_pointer]) - 2] * int(right[left_pointer])
            
            if right[left_pointer] == '1':
                flag = True
                result += 1
            
            n -= 1
            right_pointer = len(right) - 1
            
            left_pointer += 1
        
        if flag:
            result -= 1
        return result