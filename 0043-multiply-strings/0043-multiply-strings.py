class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        int_form_of_num1 = 0
        
        #To change num1, which is a string, to the integer having the same characters i.e : changing '123' to 123
        for int_character in num1:
            
            """By using ASCII number of string format of the digits and using 
            decimal place of the integer.because 10 times the number 
            increases the decimal number by one """
            int_form_of_num1 = int_form_of_num1 * 10 + (ord(int_character) - 48)

        int_form_of_num2 = 0
        
        #To change num2, which is a string, to the integer having the same characters i.e : changing '123' to 123
        for int_character in num2:
            
            """By using ASCII number of string format of
            the digits and using decimal point of the integer because
            10 times the number increases the decimal number by one """
            int_form_of_num2 = int_form_of_num2 * 10 + ord(int_character) - 48
        
        #They are now integers
        product = int_form_of_num1 * int_form_of_num2)
        
        return str(product)
