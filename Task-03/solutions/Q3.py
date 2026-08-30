"""217. Contains Duplicate
Solved Easy
 This solution converts the list into a set to strip away duplicate values, then checks if the size of the unique set is smaller than the original list.


 class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))                                   # set(nums) removes duplicates; if its length is different from the original list, duplicates existed
        
        
