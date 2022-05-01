from collections import defaultdict


class UndergroundSystem:
    def __init__(self):
        self.check_in = {}
        self.travel_history = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, s_time = self.check_in[id]
        time_btw = t - s_time
        self.travel_history[self.key(
            start_station, stationName)][0] += time_btw
        self.travel_history[self.key(start_station, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.travel_history[self.key(
            startStation, endStation)]
        return total_time / count

    def key(self, start_station, end_station):
        return f"{start_station}_{end_station}"


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
