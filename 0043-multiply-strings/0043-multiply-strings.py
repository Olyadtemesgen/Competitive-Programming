class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        number1 = 0
        for numberstring in num1:
            number1 = number1 * 10 + ord(numberstring) - 48

        number2 = 0

        for numberstring in num2:
            number2 = number2 * 10 + ord(numberstring) - 48
         
        return str(number1 * number2)
        