class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.now = 0
        self.dir = ["East", "North", "West", "South"]
        self.pos = [0, 0]
        self.max = [(width - 1, 0), (0, height - 1), (0, 0)]
    
    def step(self, num: int) -> None:
        
        x, y = self.pos[0] + self.direction[self.now][0] * num, self.pos[1] + self.direction[self.now][1] * num 
        
        if 0 <= x < self.w and 0 <= y < self.h: 
            self.pos = [x, y]

        else:

            if not self.now:
                num -= (self.w - self.pos[0] - 1)
                self.pos[0] = self.w - 1
        
            
            elif self.now == 1:
                num -= (self.h - self.pos[1] - 1)
                self.pos[1] = self.h - 1
       
            
            elif self.now == 2:
                num -= (self.pos[0])
          
                self.pos[0] = 0
            
            else:
                num -= self.pos[1]
                self.pos[1] = 0
            num =  num % ((self.w * 2 + self.h * 2 - 4))


            for _ in range(num):
                x, y = self.pos[0] + self.direction[self.now][0], self.pos[1] + self.direction[self.now][1]

                if x < 0 or y < 0 or x > self.w - 1 or y > self.h - 1:
                    self.now = (self.now + 1) % 4
                    x, y = self.pos[0] + self.direction[self.now][0], self.pos[1] + self.direction[self.now][1]
                    if not x < 0 and not y < 0 and not x > self.w - 1 and not y > self.h - 1:
                        self.pos = [x, y]
                
                else:
                    self.pos = [x, y]
    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.dir[self.now]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()