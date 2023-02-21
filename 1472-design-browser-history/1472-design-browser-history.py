class BrowserHistory:

    def __init__(self, homepage: str):
        
        self.homepage = homepage
        self.forwards = []
        self.backward =[self.homepage]
        self.step = 0
        

    def visit(self, url: str) -> None:
        
        self.forwards = []
        
        self.backward[self.step + 1:] = []
        
        self.backward.append(url)
        self.step += 1
        self.homepage = url

    def back(self, steps: int) -> str:
        
        self.step = max(self.step - steps, 0)
        return self.backward[self.step] 
        

    def forward(self, steps: int) -> str:
        
        self.step = min(steps + self.step, len(self.backward) - 1)
        return self.backward[self.step]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)