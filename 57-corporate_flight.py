class Solution:
    def corpFlightBookings(self, bookings=[], n=0 ) -> list[int]:
        result = [0] * n
        nn = 0
        for booking in bookings:
            result[booking[0] - 1] += booking[2]
            if booking[1] < n:result[booking[1]] -= booking[2]
        for x in range(1, len(result)):
            result[x] += result[x - 1]
        return result
