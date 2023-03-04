class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        position_speed = []
        stack = []
        for index in range(len(position)):
            position_speed.append([position[index], speed[index]])

        position_speed.sort(reverse=True)  

        for position, speed in position_speed:
            
            t = (target - position) / speed
            stack.append(t)
            
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        
        return len(stack)