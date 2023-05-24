class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        five = []
        ten = []
        
        for bill in bills:
            if bill == 5:
                five.append(1)
            
            elif bill == 10:
                if not five:
                    return False
                
                five.pop()
                ten.append(1)
            
            else:
                if ten:
                    ten.pop()
                    if not five:
                        return False
                    
                    five.pop()
                
                else:
                    if len(five) < 3:
                        return False
                    
                    five.pop()
                    five.pop()
                    five.pop()
        
        return True