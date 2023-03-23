class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        result = set()
        if len(s) > 12:
            return []
        
        def find_all(p1, p2, p3):
            
            nonlocal result
            if p1 >= p2 or p2 >= p3 or p3 >= len(s):
                return
            
            if int(s[:p1]) >= 256 or int(s[p1:p2]) >= 256 or int(s[p2:p3]) >= 256:
                return
            
            ans = s[:p1]+"."+ s[p1:p2]+"." +s[p2:p3]+"."+s[p3:]
            
            truth1 = (p1 > 1 and (s[0] == "0"))
            truth2 = (p2 -p1 > 1 and  s[p1] == "0")
            truth3 = (p3 - p2 > 1 and s[p2] == "0")
            truth4 = (p3 < len(s) - 1 and s[p3] == "0")
            
            real_truth = not (truth1 or truth2 or truth3 or truth4)
            
            if real_truth and int(s[:p1]) < 256 and int(s[p1:p2]) < 256 and int(s[p2:p3]) < 256 and int(s[p3:]) < 256:
                   
                result.add(ans)
            
            find_all(p1, p2, p3 + 1)
            find_all(p1, p2 + 1, p3)
            find_all(p1 + 1, p2, p3)
        
        find_all(1, 2, 3)
        
        return result