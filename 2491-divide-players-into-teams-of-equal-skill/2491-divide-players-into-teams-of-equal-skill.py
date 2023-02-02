class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        left = 0
        right = len(skill) - 1
        
        flag = skill[left] + skill[right]
        
        result = 0
        while left < right:
            
            if skill[left] + skill[right] != flag:
                return -1
            
            else:
                result += skill[left] * skill[right]
            
            left += 1
            right -= 1
        
        return result