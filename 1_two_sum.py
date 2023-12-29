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
    
# O(n) time complexity solutionL 46 ms
from typing import List

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numMap = {}
        n = len(nums)

        for index, value in enumerate(nums):
            numMap[value] = index
        
        for i in range(n):
            difference = target - nums[i]
            if difference in numMap and numMap[difference] != i:
                return [i, numMap[difference]]
        return []

# O(n) time complexity, one pass through hash map: 69 ms
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numMap = {}
        n = len(nums)

        for index in range(n):
            difference = target - nums[index]
            if difference in numMap:
                return [numMap[difference], index]
            numMap[nums[index]] = index
        
        return []