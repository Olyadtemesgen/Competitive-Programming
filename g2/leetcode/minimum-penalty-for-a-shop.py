class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        # submission
        y_n = []

        y = 0
        n = 0
        for i in customers:
            y += i == "Y"
            n += i == "N"

            y_n.append([y, n])
        
        answer = inf
        index = -1
        for i in range(len(customers)):

            if i == 0:
                answer = y_n[-1][0]
                index = 0
            
            else:
                number = y_n[i - 1][1] + (y_n[-1][0] - y_n[i - 1][0])

                if number < answer:
                    answer = number
                    index = i
         
        if y_n[-1][1] < answer:
            return len(customers)
        
        return index
        
                
               
