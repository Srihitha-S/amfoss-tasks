"""412. Fizz Buzz
Solved Easy
This solution loops through numbers from 1 to n and uses the remainder operator (%) to replace numbers with "Fizz" if divisible by 3, "Buzz" if divisible by 5, or "FizzBuzz" if divisible by both. 


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:                                  #If divisible by both 3 and 5, add "FizzBuzz"
                result.append("FizzBuzz")
            elif i % 3 == 0:                                               # If only divisible by 3, add "Fizz"
                result.append("Fizz")
            elif i % 5 == 0:                                                # If only divisible by 5, add "Buzz"
                result.append("Buzz")
            else:                                              
                result.append(str(i))                                        # If not divisible by 3 or 5, add the number itself as a string
        return result   
