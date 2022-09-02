class Solution(object):
    def fizzBuzz(self, n):
        new_list = []
        for nums in range(1, n + 1):
            if nums % 5 == 0 and nums % 3 == 0:
                new_list.append("FizzBuzz") 
                break # this break statement helps us to break the program after executing the above program
            if nums % 3 == 0:
                new_list.append("Fizz")
            elif nums % 5 == 0:
                new_list.append("Buzz") 
            else:
                new_list.append(str(nums))
        return new_list
