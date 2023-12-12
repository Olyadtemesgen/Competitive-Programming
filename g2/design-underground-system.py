class UndergroundSystem:

    def __init__(self):
        self.dictt = defaultdict(lambda: ("", 0))
        self.answer = defaultdict(lambda: [0, 0])


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.dictt[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, tt = self.dictt[id]
        one, two = self.answer[(start, stationName)]
        self.answer[(start, stationName)] =  [1 + one, t - tt + two]
        print(self.answer[(start, stationName)])
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        return ( self.answer[(startStation, endStation)][1] / self.answer[(startStation, endStation)][0])

        return 0


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)