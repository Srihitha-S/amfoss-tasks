"""9.Palindrome numbers
Solved Easy
This solution converts the integer into a string, reverses it using slicing, and checks if it matches the original string to determine if it reads the same backward and forward.compare it to the original string.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        if x[::-1]==x:                        # [::-1] reverses the string; if the reversed string matches the original, it is a palindrome
        
            return True
        else:
            return False
