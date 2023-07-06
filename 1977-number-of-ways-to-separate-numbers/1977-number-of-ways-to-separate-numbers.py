class Solution:
    
    def numberOfCombinations(self, num: str) -> int:
        
        length = len(num)
        
        dp_prefix = [[0] * (length + 1) for _ in range(length + 1)]
        
        if num[0] == "0":
            return 0
        
        for index in range(length):
            for lengt in range(1, index + 2):
                
                starting_point = index - lengt + 1
                
                current = 0
                if num[starting_point] == "0":
                    current = 0
                
                elif not starting_point:
                    current = 1
                 
                else:

                    if starting_point < lengt:
                        current = dp_prefix[starting_point - 1][starting_point]
                        
                    elif num[starting_point - lengt:starting_point] <= num[starting_point:index + 1]:
                        current = dp_prefix[starting_point - 1][lengt]

                    else:
                        current = dp_prefix[starting_point - 1][lengt - 1]

                dp_prefix[index][lengt] = dp_prefix[index][lengt - 1] + current
        

        return dp_prefix[length - 1][length] % (10 ** 9 + 7)
    