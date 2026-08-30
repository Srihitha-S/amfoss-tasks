"""442. Find all duplicates in an array
Solved medium
This solution uses a tracking set to remember numbers as it loops through the array, catching and collecting any number that appears a second time.

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()     
        duplicates = []    

        for num in nums:
            if num in seen:
                duplicates.append(num)                                   # If the number is already in our set, it is a duplicate
            else:
                seen.add(num)                                            # If it's a new number, save it in the set for later checks

        return duplicates
        
