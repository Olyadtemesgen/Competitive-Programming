class Solution:
    def daysBetweenDates2(self, date1: str, date2: str) -> int:
        
        ans1 = 0
        
        ans1 = int(date1[:4]) * 365 + int(date1[5:7]) * 30 + int(date1[8:]) 
        ans2 = int(date2[:4]) * 365 + int(date2[5:7]) * 30 + int(date2[8:])
        
        return abs(ans1 - ans2)

    
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def f(date):
            y, m, d = map(int, date.split('-'))
            if m < 3:
                m += 12
                y -= 1
            return 365 * y + y // 4 + y // 400 - y // 100 + d + (153 * m + 8) // 5
        
        return abs(f(date1) - f(date2))