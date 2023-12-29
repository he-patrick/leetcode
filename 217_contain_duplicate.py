# O(n) time complexity
# O(n) space complexity

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        for value in nums:
            if value in mySet:
                return True
            mySet.add(value)
        
        return False