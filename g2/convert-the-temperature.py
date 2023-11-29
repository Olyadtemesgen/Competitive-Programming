class Solution:
    def convertTemperature(self, Celsius: float) -> List[float]:
        return [Celsius + 273.15, Celsius * 1.80 + 32.00]
        