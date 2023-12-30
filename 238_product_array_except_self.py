# O(n) time complexity
# O(n) space complexity

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [1]*(l := len(nums)), [1]*l
        
        for i in range(1, l):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            postfix[-i - 1] = postfix[-i] * nums[-i]
        for index, (lv, rv) in enumerate(zip(prefix, postfix)):
            nums[index] = lv*rv

        return nums
    
# O(n) time complexity
# O(1) space complexity

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        result = [1] * l

        prefix = 1
        for i in range(l):
            result[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for j in range(l - 1, -1, -1):
            result[j] *= postfix
            postfix *= nums[j]

        return result
