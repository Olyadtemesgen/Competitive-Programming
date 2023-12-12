class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tokens = defaultdict(int)
        self.time = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.time

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.time 

    def countUnexpiredTokens(self, currentTime: int) -> int:

        answer = 0

        for token in self.tokens:
            if self.tokens[token] > currentTime:
                answer += 1
        
        return answer
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)