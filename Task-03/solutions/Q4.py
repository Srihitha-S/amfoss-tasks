"""151. Reverse words in string
Solved medium
This solution splits the string into a list of words to automatically strip extra spaces, reverses the list, and joins the words back together with a single space.

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()                                                       # Splits the string into a list of words and automatically removes all extra spaces

        reversed_words = words[::-1]                                            # Reverses the order of the words in the list

        return " ".join(reversed_words)                                          # Joins the reversed words back into a single string, separated by a space
        
