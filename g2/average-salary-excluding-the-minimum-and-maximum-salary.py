class Solution:
    def average(self, salary: List[int]) -> float:
        
        if len(salary) < 3:
            return 0
        
        maxx = max(salary)
        minn = min(salary)
            
        summ = sum(salary) - minn - maxx
        average = summ / (len(salary) - 2)

        return average