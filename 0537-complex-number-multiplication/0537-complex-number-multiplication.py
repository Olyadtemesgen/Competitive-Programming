class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        numm1 = [num1[0]]
        numm2 = [num2[0]]
        
        for index, x in enumerate(num1[1:]):
            
            if x not in '+i':
                numm1[-1] += x
            
            elif x == '+':
                numm1.append('')
        
        if '+' not in num1 and 'i' in num1:
            numm1 = ['0'] + numm1
        
        elif '+' not in num1: 
            numm1.append('0')
        for index, x in enumerate(num2[1:]):
            
            if x not in '+i':
                numm2[-1] += x
            
            elif x == '+':
                numm2.append('')
        
        if '+' not in num2 and 'i' in num2:
            numm2 = ['0'] + numm2
        
        elif '+' not in num2: 
            numm2.append('0')
        
        constant = str(int(numm1[0]) * int(numm2[0]) - int(numm1[1]) *int(numm2[1]))
        
        imaginary = str(int(numm1[1]) * int(numm2[0]) + int(numm1[0]) * int(numm2[1]))
        
        return constant + '+' + imaginary + 'i'