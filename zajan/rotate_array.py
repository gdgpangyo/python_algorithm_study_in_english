# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/

class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        cpy = nums[:]
        l = len(nums)
        for i in range(0, l):
            nums[(i+k) % l] = cpy[i]

# TestCase
sol = Solution()
nums = [1,2,3,4,5,6,7]
sol.rotate(nums, 3)
print(nums)
