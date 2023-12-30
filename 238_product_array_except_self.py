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