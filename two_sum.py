# O(n^2) time complexity solution: 55 ms

from typing import List

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arrLength = len(nums)
        
        for i in range(arrLength - 1):
            for j in range(i + 1, arrLength):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
# O(n) time complexity solution

class Solution2:
    def twoSum(self )